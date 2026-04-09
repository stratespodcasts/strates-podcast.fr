import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

FEEDS = [
    {
        "url": "https://feed.ausha.co/BD34s8Q9XL4b",
        "show": "Good Morning la Galaxie",
        "cover": "/images/goodmorning.png"
    },
    {
        "url": "https://feed.ausha.co/owE9IqM4EWgb",
        "show": "Candide en Vers",
        "cover": "/images/candide.png"
    }
]

episodes = []

for feed in FEEDS:
    try:
        print(f"Fetching {feed['show']}...")
        req = urllib.request.Request(feed["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
        for item in root.findall(".//item"):
            enc = item.find("enclosure")
            if enc is None:
                continue
            title_el = item.find("title")
            pubdate_el = item.find("pubDate")
            duration_el = item.find("itunes:duration", ns)
            title = title_el.text.strip() if title_el is not None else ""
            audio_url = enc.get("url", "")
            duration = duration_el.text.strip() if duration_el is not None else ""
            try:
                dt = parsedate_to_datetime(pubdate_el.text) if pubdate_el is not None else datetime(1970, 1, 1, tzinfo=timezone.utc)
                date_iso = dt.isoformat()
                date_ts = dt.timestamp()
            except Exception:
                date_iso = ""
                date_ts = 0
            episodes.append({
                "title": title,
                "show": feed["show"],
                "cover": feed["cover"],
                "url": audio_url,
                "duration": duration,
                "date": date_iso,
                "ts": date_ts
            })
        print(f"  -> {len([e for e in episodes if e['show'] == feed['show']])} episodes")
    except Exception as e:
        print(f"  ERREUR {feed['show']}: {e}")

episodes.sort(key=lambda e: e["ts"], reverse=True)

import os
os.makedirs("static", exist_ok=True)
with open("static/episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)

print(f"\nTotal : {len(episodes)} episodes -> static/episodes.json")
