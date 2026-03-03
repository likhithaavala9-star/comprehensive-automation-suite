import requests
import random
import time
import logging
import json
import csv
from bs4 import BeautifulSoup
import urllib3
import os


# Disable SSL warnings (only for development)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "scraped_data.json")
csv_path = os.path.join(base_dir, "scraped_data.csv")

from automation_suite.utils import setup_logging

setup_logging()


class WebScraper:

    def __init__(self):
        self.stats = {
            "requests_made": 0,
            "success": 0,
            "failed": 0
        }

        # Rotate User Agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
        ]

    def scrape(self, url, retries=3):
        for attempt in range(retries):
            try:
                headers = {
                    "User-Agent": random.choice(self.user_agents)
                }

                logging.info(f"Scraping URL: {url}")
                response = requests.get(
                    url,
                    headers=headers,
                    timeout=10,
                    verify=False  # Disable SSL verification (development only)
                )

                self.stats["requests_made"] += 1

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    headings = [h.text.strip() for h in soup.find_all("h1")]

                    logging.info(f"Found {len(headings)} headings")
                    self.stats["success"] += 1

                    # Rate limiting
                    time.sleep(2)

                    return headings
                else:
                    logging.warning(f"Status code: {response.status_code}")

            except Exception as e:
                logging.error(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(2)

        self.stats["failed"] += 1
        return []

    def export_data(self, data, filename="scraped_data"):
        if not data:
            logging.warning("No data to export.")
            return

        # Export JSON
        with open(f"{filename}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        logging.info("Data exported to JSON.")

        # Export CSV
        with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title"])
            for item in data:
                writer.writerow([item])

        logging.info("Data exported to CSV.")


if __name__ == "__main__":
    scraper = WebScraper()

    # Test URL
    url = "https://invalid-url-test-12345.com"

    titles = scraper.scrape(url)

    print("\nScraped Titles:\n")
    for t in titles:
        print("-", t)

    scraper.export_data(titles)

    print("\nStats:", scraper.stats)
