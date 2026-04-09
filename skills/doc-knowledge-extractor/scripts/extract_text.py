#!/usr/bin/env python3
"""
doc-knowledge-extractor: extract_text.py
使用 macOS textutil 提取 PDF/DOCX/HTML/TXT 文本
"""

import sys
import os
import tempfile
import subprocess
import argparse
import json


def extract_with_textutil(input_path: str) -> str:
    """用 textutil 把文档转成 txt（macOS 自带）"""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"文件不存在: {input_path}")
    
    # textutil -convert txt -stdout input.pdf
    result = subprocess.run(
        ['textutil', '-convert', 'txt', '-stdout', input_path],
        capture_output=True,
        text=True,
        timeout=60
    )
    if result.returncode != 0:
        raise RuntimeError(f"textutil 失败: {result.stderr}")
    return result.stdout


def extract_by_extension(path: str) -> str:
    """根据扩展名直接读取纯文本文件"""
    ext = os.path.splitext(path)[1].lower()
    if ext == '.txt':
        with open(path, 'utf-8') as f:
            return f.read()
    elif ext == '.md':
        with open(path, 'utf-8') as f:
            return f.read()
    elif ext == '.json':
        with open(path, 'utf-8') as f:
            data = json.load(f)
            return json.dumps(data, ensure_ascii=False, indent=2)
    else:
        return extract_with_textutil(path)


def main():
    parser = argparse.ArgumentParser(description='提取文档文本')
    parser.add_argument('input', help='输入文件路径')
    parser.add_argument('--output', '-o', help='输出文件路径（默认 stdout）')
    parser.add_argument('--max-chars', '-m', type=int, default=None, help='最大字符数')
    args = parser.parse_args()

    text = extract_by_extension(args.input)
    
    if args.max_chars and len(text) > args.max_chars:
        text = text[:args.max_chars] + f"\n\n[...截断，原始长度 {len(text)} 字符]"
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"已保存至: {args.output} ({len(text)} 字符)")
    else:
        print(text)


if __name__ == '__main__':
    main()
