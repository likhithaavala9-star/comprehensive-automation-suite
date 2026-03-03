from automation_suite.modules.web_scraper import WebScraper
from automation_suite.modules.email_automation import EmailAutomation
import logging
from automation_suite.utils import setup_logging

setup_logging()


def run_scraper_email_pipeline():
    try:
        logging.info("Starting Scraper + Email pipeline")

        scraper = WebScraper()
        emailer = EmailAutomation()

        url = "https://example.com"
        headings = scraper.scrape(url)

        if not headings:
            logging.warning("No data scraped. Email not sent.")
            return

        body = "Scraped Headings:\n\n"
        for h in headings:
            body += f"- {h}\n"

        emailer.send_email(
            "nanciesuresh@gmail.com",
            "Daily Scraped Report",
            body
        )

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_scraper_email_pipeline()
