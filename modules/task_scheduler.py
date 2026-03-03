import json
import time
import logging
import schedule

from automation_suite.utils import setup_logging
from automation_suite.modules.web_scraper import WebScraper
from automation_suite.modules.email_automation import EmailAutomation
from automation_suite.modules.system_monitor import SystemMonitor

setup_logging()


class TaskScheduler:

    def __init__(self, config_path="automation_suite/configs/schedules.json"):
        self.config_path = config_path

    def load_tasks(self):
        with open(self.config_path, "r") as f:
            data = json.load(f)
        return data["tasks"]

    def run_scraper(self):
        logging.info("Running scheduled Scraper...")

        from automation_suite.modules.web_scraper import WebScraper
        scraper = WebScraper()

        url = "https://example.com"
        headings = scraper.scrape(url)

        if headings:
             logging.info("Headings found. Triggering email...")
             self.run_email()
        else:
             logging.warning("No headings found. Email not triggered.")


    def run_email(self):
        logging.info("Running scheduled Email...")
        emailer = EmailAutomation()
        emailer.send_email(
            receiver_email="nanciesuresh@gmail.com",
            subject="Scheduled Email",
            body="This is an automated scheduled email."
        )

    def run_monitor(self):
        logging.info("Running scheduled System Monitor...")
        monitor = SystemMonitor()
        monitor.display_stats()

    def schedule_tasks(self):
        tasks = self.load_tasks()

        for task in tasks:
            if not task.get("enabled", True):
                logging.info(f"Task {task['name']} is disabled.")
                continue

            if task["module"] == "web_scraper":
                 schedule.every(task["interval"]).seconds.do(self.run_scraper)

            elif task["module"] == "email_automation":
                 schedule.every(task["interval"]).seconds.do(self.run_email)

            elif task["module"] == "system_monitor":
                 schedule.every(task["interval"]).seconds.do(self.run_monitor)

        logging.info("All enabled tasks scheduled successfully.")

    def start(self):
        logging.info("Task Scheduler Started...")
        print("Task Scheduler Started...\n")

        self.schedule_tasks()
        self.running = True

        try:
            while self.running:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        logging.info("Scheduler stopped manually.")
        print("Scheduler stopped.")
 
    def stop(self):
        self.running = False
        schedule.clear()
        logging.info("Scheduler stopped via GUI.")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.start()
