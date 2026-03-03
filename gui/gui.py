import tkinter as tk
import threading
from tkinter import messagebox
from automation_suite.modules.web_scraper import WebScraper
from automation_suite.modules.email_automation import EmailAutomation
from automation_suite.modules.system_monitor import SystemMonitor
from automation_suite.modules.workflow_designer import WorkflowDesigner
from automation_suite.modules.task_scheduler import TaskScheduler


class AutomationGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Automation Suite")
        self.root.geometry("500x500")
        self.scheduler = TaskScheduler()
        self.scheduler_thread = None

        self.create_widgets()

    def start_scheduler(self):
        if not self.scheduler_thread or not self.scheduler_thread.is_alive():
            self.update_status("Scheduler Running", "orange")
            self.scheduler_thread = threading.Thread(target=self.scheduler.start)
            self.scheduler_thread.daemon = True
            self.scheduler_thread.start()
        else:
            self.update_status("Scheduler Already Running", "blue")


    def create_widgets(self):

        tk.Label(self.root, text="Automation Suite Control Panel",
                 font=("Arial", 16, "bold")).pack(pady=20)

        tk.Button(self.root, text="Run File Organizer",
                  width=30, command=self.run_file_organizer).pack(pady=5)

        tk.Button(self.root, text="Run Web Scraper",
                  width=30, command=self.run_scraper).pack(pady=5)

        tk.Button(self.root, text="Send Email",
                  width=30, command=self.run_email).pack(pady=5)

        tk.Button(self.root, text="Run System Monitor",
                  width=30, command=self.run_monitor).pack(pady=5)

        tk.Button(self.root, text="Start Task Scheduler",
                  width=30, command=self.start_scheduler).pack(pady=5)

        tk.Button(self.root, text="Run Workflow",
                  width=30, command=self.run_workflow).pack(pady=5)
    
        tk.Button(self.root, text="Stop Task Scheduler", 
                  width = 30, command=self.stop_scheduler).pack(pady=5)

        self.status_label = tk.Label(self.root, text="Status: Ready",
                                     fg="green")
        self.status_label.pack(pady=20)

    def run_file_organizer(self):
        messagebox.showinfo("Info", "File Organizer triggered!")

    def run_scraper(self):
        threading.Thread(target=self._run_scraper).start()

    def _run_scraper(self):
        self.update_status("Running Scraper...", "blue")
        scraper = WebScraper()
        scraper.scrape("https://example.com")
        self.update_status("Scraper Finished")

    def run_email(self):
        threading.Thread(target=self._run_email).start()

    def _run_email(self):
        self.update_status("Sending Email...")
        emailer = EmailAutomation()
        emailer.send_email(
            receiver_email="nanciesuresh@gmail.com",
            subject="GUI Email",
            body="This email was sent from GUI."
        )
        self.update_status("Email Sent")

    def run_monitor(self):
        threading.Thread(target=self._run_monitor).start()

    def _run_monitor(self):
        self.update_status("Running System Monitor...")
        monitor = SystemMonitor()
        monitor.display_stats()
        self.update_status("Monitor Finished")

    def run_scheduler(self):
            messagebox.showinfo("Info", "Scheduler triggered!")

    def run_workflow(self):
           threading.Thread(target=self._run_workflow).start()

    def _run_workflow(self):
        self.update_status("Running Workflow...")
        workflow = WorkflowDesigner()
        workflow.run_workflow("Scrape and Email")
        self.update_status("Workflow Completed")

    def update_status(self, message, color="green"):
        self.status_label.config(text=f"Status: {message}", fg=color)

    def stop_scheduler(self):
        self.scheduler.stop()
        self.update_status("Scheduler Stopped", "green")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AutomationGUI()
    app.run()
