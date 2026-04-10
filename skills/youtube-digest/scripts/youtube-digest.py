#!/usr/bin/env python3
"""
youtube-digest.py — Daily YouTube video digest
Uses youtube-transcript-api (free, no API key needed).
"""

import sys
import json
import argparse
import re
from urllib.parse import urlparse, parse_qs

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )
    _yta = YouTubeTranscriptApi()
except ImportError:
    print(json.dumps({"ok": False, "error": "youtube-transcript-api not installed. Run: pip install youtube-transcript-api"}))
    sys.exit(1)


def extract_video_id(url_or_id: str) -> str:
    """Extract 11-char video ID from URL or return as-is if already an ID."""
    url_or_id = url_or_id.strip()
    if len(url_or_id) == 11 and not url_or_id.startswith("http"):
        return url_or_id
    parsed = urlparse(url_or_id)
    if parsed.hostname in ("youtu.be", "youtube.com", "www.youtube.com"):
        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/shorts/")[1][:11]
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0][:11]
        if parsed.path.startswith("/embed/") or parsed.path.startswith("/v/"):
            return parsed.path.split("/")[-1][:11]
    return url_or_id[:11]


def get_transcript(video_id: str) -> dict:
    """Fetch transcript for a video."""
    try:
        transcript_list = _yta.list(video_id)
        try:
            transcript = transcript_list.find_transcript(["en"])
        except Exception:
            transcript = transcript_list.find_generated_transcript(["en"])
        
        full_text = " ".join([
            f"[{int(e.start)}s] {e.text}"
            for e in transcript.fetch()
        ])
        return {
            "ok": True,
            "video_id": video_id,
            "language": transcript.language_code,
            "transcript": full_text[:5000],  # Limit to first 5000 chars
            "metadata": {"video_id": video_id}
        }
    except TranscriptsDisabled:
        return {"ok": False, "error": f"Transcripts disabled for {video_id}"}
    except NoTranscriptFound:
        return {"ok": False, "error": f"No transcript found for {video_id}"}
    except VideoUnavailable:
        return {"ok": False, "error": f"Video unavailable: {video_id}"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def get_channel_latest(channel: str, limit: int = 3) -> dict:
    """Get latest videos from a channel by scraping the channel page."""
    try:
        import urllib.request
        
        if channel.startswith("@"):
            url = f"https://www.youtube.com/{channel}/videos"
        elif "/channel/" in channel:
            url = channel.split("/videos")[0] + "/videos"
        elif "/@" in channel:
            url = channel.split("/videos")[0] + "/videos"
        else:
            url = f"https://www.youtube.com/{channel}/videos"
        
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8", errors="ignore")
        
        # Find video IDs and titles from JSON in the page
        video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
        
        # Deduplicate while preserving order
        seen = set()
        unique_ids = []
        for vid in video_ids:
            if vid not in seen:
                seen.add(vid)
                unique_ids.append(vid)
        
        # Titles appear in JSON structure near videoIds
        title_pattern = re.findall(r'"title":\{"runs":\[\{"text":"([^"]{1,200})"\}\]\}', html)
        
        videos = []
        for i, vid in enumerate(unique_ids[:limit]):
            title = title_pattern[i] if i < len(title_pattern) else f"Video {vid}"
            videos.append({
                "video_id": vid,
                "title": title,
                "url": f"https://www.youtube.com/watch?v={vid}"
            })
        
        return {"ok": True, "channel": channel, "videos": videos}
    
    except Exception as e:
        return {"ok": False, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="YouTube Digest CLI")
    sub = parser.add_subparsers(dest="cmd")
    
    trans_parser = sub.add_parser("transcript", help="Get transcript for a video")
    trans_parser.add_argument("video", help="Video URL or ID")
    
    latest_parser = sub.add_parser("latest", help="Get latest videos from a channel")
    latest_parser.add_argument("channel", help="Channel URL, @handle, or ID")
    latest_parser.add_argument("--limit", type=int, default=3)
    
    args = parser.parse_args()
    
    if args.cmd == "transcript":
        video_id = extract_video_id(args.video)
        result = get_transcript(video_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.cmd == "latest":
        result = get_channel_latest(args.channel, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
