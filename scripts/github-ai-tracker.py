#!/usr/bin/env python3
"""
GitHub AI 板块 trending 监控脚本
监控 AI/ML 相关仓库的 star增长、下载量突增
"""

import subprocess
import json
import os
import re
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.openclaw/workspace/github-ai-tracker/history.json")
ALERTS_FILE = os.path.expanduser("~/.openclaw/workspace/github-ai-tracker/alerts.json")

def get_github_search_results(query="AI model language learning", days=1, limit=30):
    """通过 GitHub API 搜索 AI 相关仓库"""
    import urllib.request
    import urllib.parse
    
    # 搜索最近活跃的 AI 仓库
    search_queries = [
        "AI model in:readme created:>2025-01-01 stars:>100",
        "language model in:readme created:>2025-01-01 stars:>500", 
        "artificial intelligence in:readme pushed:>2026-04-01 stars:>200",
    ]
    
    results = []
    for q in search_queries:
        try:
            url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=50"
            req = urllib.request.Request(url, headers={'User-Agent': 'OpenClaw-Tracker/1.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                results.extend(data.get('items', []))
        except Exception as e:
            print(f"API error: {e}")
    
    # 去重
    seen = set()
    unique = []
    for r in results:
        if r['full_name'] not in seen:
            seen.add(r['full_name'])
            unique.append(r)
    return unique[:limit]

def get_trending_html():
    """抓取 GitHub Trending 页面"""
    import urllib.request
    try:
        url = "https://github.com/trending?since=daily"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        print(f"Trending fetch error: {e}")
        return ""

def parse_trending_stars(html):
    """从 trending 页面解析 star 数量"""
    pattern = r'<a href="/([^"]+)" class="Link Link--muted[^"]*">\s*([\d,]+)\s*stars</a>'
    matches = re.findall(pattern, html)
    return {name: int(stars.replace(',', '')) for name, stars in matches}

def load_history():
    """加载历史数据"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return {}

def save_history(history):
    """保存历史数据"""
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def load_alerts():
    """加载已有告警"""
    if os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE) as f:
            return json.load(f)
    return []

def save_alerts(alerts):
    """保存新告警"""
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)
    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)

def check_surge(repo_name, current_stars, history):
    """检测 star 是否突增"""
    if repo_name in history:
        prev_stars = history[repo_name]['stars']
        growth = current_stars - prev_stars
        growth_pct = (growth / prev_stars * 100) if prev_stars > 0 else 0
        return growth, growth_pct
    return 0, 0

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running GitHub AI tracker...")
    
    # 获取 trending 数据
    trending_html = get_trending_html()
    trending_repos = parse_trending_stars(trending_html)
    
    # 获取 API 搜索结果
    api_repos = get_github_search_results()
    
    # 加载历史
    history = load_history()
    alerts = load_alerts()
    
    new_alerts = []
    report_lines = []
    report_lines.append(f"\n{'='*60}")
    report_lines.append(f"GitHub AI Tracker Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report_lines.append(f"{'='*60}\n")
    
    # 检测 trending 突增
    report_lines.append("📈 Trending 突增检测:")
    for repo, stars in trending_repos.items():
        growth, growth_pct = check_surge(repo, stars, history)
        if growth > 50 and growth_pct > 20:  # 阈值
            alert = f"🔥 {repo}: +{growth} stars ({growth_pct:.0f}%) → {stars} total stars"
            new_alerts.append({
                'repo': repo,
                'type': 'trending_surge',
                'growth': growth,
                'growth_pct': growth_pct,
                'total_stars': stars,
                'time': datetime.now().isoformat()
            })
            report_lines.append(f"  {alert}")
        history[repo] = {'stars': stars, 'checked': datetime.now().isoformat()}
    
    # AI 相关仓库重点关注
    ai_keywords = ['ai', 'llm', 'gpt', 'claude', 'model', 'neural', 'machine-learning', 'deep-learning', 'openai', 'anthropic', 'agent', 'memory']
    
    report_lines.append("\n🤖 AI 相关仓库 (API搜索):")
    for repo_data in api_repos[:20]:
        name = repo_data['full_name']
        stars = repo_data.get('stargazers_count', 0)
        desc = repo_data.get('description', '') or ''
        lang = repo_data.get('language', '') or ''
        pushed = repo_data.get('pushed_at', '')[:10]
        
        # 标记 AI 相关
        is_ai = any(k in (name + desc).lower() for k in ai_keywords)
        
        growth, growth_pct = check_surge(name, stars, history)
        
        marker = "🤩" if is_ai else "  "
        if is_ai and (growth > 100 or growth_pct > 15):
            alert = f"  {marker} **{name}**: {stars:,} stars (+{growth}, +{growth_pct:.0f}%) | {desc[:60]}"
            new_alerts.append({
                'repo': name,
                'type': 'ai_surge',
                'growth': growth,
                'growth_pct': growth_pct,
                'total_stars': stars,
                'description': desc,
                'language': lang,
                'pushed': pushed,
                'time': datetime.now().isoformat()
            })
            report_lines.append(alert)
        
        # 更新历史
        if name not in history or stars != history[name].get('stars'):
            history[name] = {'stars': stars, 'checked': datetime.now().isoformat()}
    
    # 合并告警（去重）
    existing_repos = {a['repo'] for a in alerts}
    for alert in new_alerts:
        if alert['repo'] not in existing_repos:
            alerts.insert(0, alert)  # 插入到开头
    
    # 只保留最近30条告警
    alerts = alerts[:30]
    
    save_history(history)
    save_alerts(alerts)
    
    report_lines.append(f"\n📊 共监控 {len(history)} 个仓库")
    report_lines.append(f"🔔 新增告警: {len(new_alerts)}")
    
    report = '\n'.join(report_lines)
    print(report)
    
    # 如果有新告警，打印出来
    if new_alerts:
        print("\n" + "🔥"*20)
        print("新发现突增仓库!")
        print("🔥"*20)
        for a in new_alerts:
            print(f"  → {a['repo']}: +{a['growth']} stars ({a['growth_pct']:.0f}%)")

if __name__ == "__main__":
    main()
