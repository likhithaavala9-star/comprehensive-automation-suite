import json
import logging

from automation_suite.utils import setup_logging
from automation_suite.modules.web_scraper import WebScraper
from automation_suite.modules.email_automation import EmailAutomation
from automation_suite.modules.system_monitor import SystemMonitor

setup_logging()


class WorkflowDesigner:

    def __init__(self, config_path="automation_suite/configs/workflows.json"):
        self.config_path = config_path

    def load_workflows(self):
        with open(self.config_path, "r") as f:
            data = json.load(f)
        return data["workflows"]

    def run_workflow(self, workflow):
        logging.info(f"Starting workflow: {workflow['name']}")
        print(f"\n=== Running Workflow: {workflow['name']} ===")

        context = {}  # Store results between steps

        for step in workflow["steps"]:
            try:
                if step == "web_scraper":
                    scraper = WebScraper()
                    headings = scraper.scrape("https://example.com")
                    context["headings"] = headings

                elif step == "email_automation":
                    if context.get("headings"):
                        emailer = EmailAutomation()
                        emailer.send_email(
                            receiver_email="nanciesuresh@gmail.com",
                            subject="Workflow Email",
                            body="Scraper found headings. Email triggered."
                        )
                    else:
                        logging.info("No headings found. Email skipped.")

                elif step == "system_monitor":
                    monitor = SystemMonitor()
                    monitor.display_stats()

                logging.info(f"Step '{step}' executed successfully.")

            except Exception as e:
                logging.error(f"Error in step '{step}': {e}")
                print(f"Error executing step {step}")
                break

        print("=== Workflow Completed ===\n")
        logging.info(f"Workflow '{workflow['name']}' completed.")

    def run_enabled_workflows(self):
        workflows = self.load_workflows()

        for workflow in workflows:
            if workflow.get("enabled", True):
                self.run_workflow(workflow)

if __name__ == "__main__":
    designer = WorkflowDesigner()
    designer.run_enabled_workflows()
