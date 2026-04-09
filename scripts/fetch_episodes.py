import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime, format_datetime

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

SITE_URL = "https://strates-podcast.fr"
LABEL_TITLE = "STRATES — Le label"
LABEL_DESC = "Les Ecoutes de la Profondeur. Tous les podcasts du label STRATES reunis en un seul flux."
LABEL_COVER = "https://strates-podcast.fr/images/strates-cover.png"

episodes = []

for feed in FEEDS:
    try:
        print(f"Fetching {feed['show']}...")
        req = urllib.request.Request(feed["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}

        # Vignette par défaut du podcast (niveau channel)
        channel_image_el = root.find(".//channel/itunes:image", ns)
        channel_cover = channel_image_el.get("href") if channel_image_el is not None else feed["cover"]

        for item in root.findall(".//item"):
            enc = item.find("enclosure")
            if enc is None:
                continue
            title_el = item.find("title")
            pubdate_el = item.find("pubDate")
            duration_el = item.find("itunes:duration", ns)
            desc_el = item.find("description")
            guid_el = item.find("guid")

            # Vignette spécifique à l'épisode, sinon celle du podcast
            ep_image_el = item.find("itunes:image", ns)
            if ep_image_el is not None:
                ep_cover = ep_image_el.get("href", channel_cover)
            else:
                ep_cover = channel_cover

            title = title_el.text.strip() if title_el is not None else ""
            audio_url = enc.get("url", "")
            audio_type = enc.get("type", "audio/mpeg")
            audio_length = enc.get("length", "0")
            duration = duration_el.text.strip() if duration_el is not None else ""
            description = desc_el.text.strip() if desc_el is not None else ""
            guid = guid_el.text.strip() if guid_el is not None else audio_url

            try:
                dt = parsedate_to_datetime(pubdate_el.text) if pubdate_el is not None else datetime(1970, 1, 1, tzinfo=timezone.utc)
                date_iso = dt.isoformat()
                date_ts = dt.timestamp()
                date_rfc = format_datetime(dt)
            except Exception:
                date_iso = ""
                date_ts = 0
                date_rfc = ""

            episodes.append({
                "title": title,
                "show": feed["show"],
                "cover": ep_cover,
                "cover_fallback": feed["cover"],
                "url": audio_url,
                "audio_type": audio_type,
                "audio_length": audio_length,
                "duration": duration,
                "description": description,
                "guid": guid,
                "date": date_iso,
                "date_rfc": date_rfc,
                "ts": date_ts
            })

        count = len([e for e in episodes if e['show'] == feed['show']])
        print(f"  -> {count} episodes")
    except Exception as e:
        print(f"  ERREUR {feed['show']}: {e}")

episodes.sort(key=lambda e: e["ts"], reverse=True)

import os
os.makedirs("static", exist_ok=True)

# --- episodes.json pour le lecteur web ---
with open("static/episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)
print(f"\nTotal : {len(episodes)} episodes -> static/episodes.json")

# --- feed.xml agrégateur RSS ---
now_rfc = format_datetime(datetime.now(timezone.utc))

rss_items = ""
for ep in episodes:
    rss_items += f"""
    <item>
      <title><![CDATA[[{ep['show']}] {ep['title']}]]></title>
      <description><![CDATA[{ep['description']}]]></description>
      <enclosure url="{ep['url']}" length="{ep['audio_length']}" type="{ep['audio_type']}"/>
      <guid isPermaLink="false">{ep['guid']}</guid>
      <pubDate>{ep['date_rfc']}</pubDate>
      <itunes:duration>{ep['duration']}</itunes:duration>
      <itunes:author>{ep['show']}</itunes:author>
      <itunes:image href="{ep['cover']}"/>
    </item>"""

feed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
  xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{LABEL_TITLE}</title>
    <link>{SITE_URL}</link>
    <description>{LABEL_DESC}</description>
    <language>fr-fr</language>
    <lastBuildDate>{now_rfc}</lastBuildDate>
    <itunes:author>STRATES</itunes:author>
    <itunes:image href="{LABEL_COVER}"/>
    <itunes:category text="Arts"/>
    {rss_items}
  </channel>
</rss>"""

with open("static/feed.xml", "w", encoding="utf-8") as f:
    f.write(feed_xml)
print(f"Flux RSS agrégateur -> static/feed.xml")
