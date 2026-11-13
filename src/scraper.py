"""
Web Scraper and Knowledge Extractor for Academic Philosophy.
Extracts rigorous concepts from the Stanford Encyclopedia of Philosophy (SEP),
Internet Encyclopedia of Philosophy (IEP), and verified local primary-source archives.
"""

import os
import re
import json
import time
import urllib.parse
from pathlib import Path
from typing import Dict, List, Optional, Any
import requests
from bs4 import BeautifulSoup

CACHE_DIR = Path(__file__).resolve().parent.parent / "content" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

LOCAL_NOTES_DIR = Path("/Users/anshu_macmini/Philosophy Notes/md")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36 PhilosophyPrepBot/1.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


class PhilosophyScraper:
    """Scrapes philosophical concepts and synchronizes with primary source archives."""

    def __init__(self, delay_seconds: float = 1.0):
        self.delay = delay_seconds
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def _get_cache_path(self, key: str) -> Path:
        safe_key = re.sub(r"[^a-zA-Z0-9_\-]", "_", key).lower()
        return CACHE_DIR / f"{safe_key}.json"

    def fetch_sep_entry(self, entry_slug: str) -> Optional[Dict[str, Any]]:
        """
        Fetches an entry from the Stanford Encyclopedia of Philosophy (SEP).
        Example slugs: 'epistemology-india', 'kallipat-kant', 'nagarjuna', 'shankara'.
        """
        cache_file = self._get_cache_path(f"sep_{entry_slug}")
        if cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass

        url = f"https://plato.stanford.edu/entries/{entry_slug}/"
        try:
            resp = self.session.get(url, timeout=12)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                title_elem = soup.find("h1") or soup.find("title")
                title = title_elem.get_text(strip=True) if title_elem else entry_slug

                # Extract preamble / intro section
                content_div = soup.find("div", id="content") or soup.find("div", id="article-content")
                preamble_text = ""
                sections = []

                if content_div:
                    # Collect first few paragraphs before the first heading
                    intro_paras = []
                    for el in content_div.children:
                        if el.name in ["h2", "h3"]:
                            break
                        if el.name == "p":
                            txt = el.get_text(strip=True)
                            if txt:
                                intro_paras.append(txt)
                    preamble_text = " ".join(intro_paras[:4])

                    # Extract section titles
                    for h2 in content_div.find_all("h2"):
                        sec_text = h2.get_text(strip=True)
                        if sec_text and not sec_text.startswith("Bibliography") and not sec_text.startswith("Academic"):
                            sections.append(sec_text)

                data = {
                    "source": "Stanford Encyclopedia of Philosophy (SEP)",
                    "slug": entry_slug,
                    "url": url,
                    "title": title,
                    "preamble": preamble_text,
                    "sections": sections,
                    "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                }

                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                time.sleep(self.delay)
                return data
            else:
                return None
        except Exception as e:
            return None

    def fetch_iep_entry(self, entry_slug: str) -> Optional[Dict[str, Any]]:
        """
        Fetches an entry from the Internet Encyclopedia of Philosophy (IEP).
        Example slugs: 'advaita-vedanta', 'kant-epist', 'husserl'.
        """
        cache_file = self._get_cache_path(f"iep_{entry_slug}")
        if cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass

        url = f"https://iep.utm.edu/{entry_slug}/"
        try:
            resp = self.session.get(url, timeout=12)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                title_elem = soup.find("h1", class_="entry-title") or soup.find("title")
                title = title_elem.get_text(strip=True) if title_elem else entry_slug

                content_div = soup.find("div", class_="entry-content")
                intro_paras = []
                sections = []

                if content_div:
                    for p in content_div.find_all("p"):
                        txt = p.get_text(strip=True)
                        if len(txt) > 40:
                            intro_paras.append(txt)
                        if len(intro_paras) >= 3:
                            break

                    for h2 in content_div.find_all(["h2", "h3"]):
                        sec_text = h2.get_text(strip=True)
                        if sec_text and "References" not in sec_text and "Author" not in sec_text:
                            sections.append(sec_text)

                data = {
                    "source": "Internet Encyclopedia of Philosophy (IEP)",
                    "slug": entry_slug,
                    "url": url,
                    "title": title,
                    "preamble": " ".join(intro_paras),
                    "sections": sections,
                    "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                }

                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                time.sleep(self.delay)
                return data
            else:
                return None
        except Exception:
            return None

    def search_local_notes(self, query: str) -> List[Dict[str, Any]]:
        """
        Extracts verified primary source commentary from the local
        annotated notes directory (/Users/anshu_macmini/Philosophy Notes/md).
        """
        results = []
        if not LOCAL_NOTES_DIR.exists():
            return results

        pattern = re.compile(re.escape(query), re.IGNORECASE)
        for filepath in LOCAL_NOTES_DIR.glob("*.md"):
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Search for entries with '> **Author, *Title*'
                entries = content.split("\n> **")
                for item in entries[1:]:
                    block = "> **" + item
                    if pattern.search(block):
                        # Extract the block up to the next horizontal rule or next header
                        clean_block = block.split("\n---")[0].strip()
                        lines = clean_block.splitlines()
                        header = lines[0].strip() if lines else ""
                        results.append({
                            "source_file": filepath.name,
                            "header": header,
                            "text": clean_block,
                        })
            except Exception:
                continue

        return results


if __name__ == "__main__":
    scraper = PhilosophyScraper()
    print("Testing local primary notes indexer...")
    local_hits = scraper.search_local_notes("prāmāṇya")
    print(f"Found {len(local_hits)} local notes entries for 'prāmāṇya'")
    for h in local_hits[:2]:
        print(f"- {h['source_file']}: {h['header'][:80]}...")
