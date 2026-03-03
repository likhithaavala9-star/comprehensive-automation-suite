import smtplib
import schedule
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from automation_suite.utils import setup_logging

setup_logging()


class EmailAutomation:

    def __init__(self):
        self.sender_email = "likhithaavala9@gmail.com"
        self.password = "atzwpfooyisojrhz"
        self.smtp_server = "smtp.gmail.com"
        self.port = 587

    def send_email(self, receiver_email, subject, body):
        try:
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)
            server.quit()

            logging.info(f"Email sent successfully to {receiver_email}")
            print("Email sent successfully!")

        except Exception as e:
            logging.error(f"Email sending failed: {e}")
            print("Failed to send email:", e)


# 🔥 Scheduler job must be AFTER the class
def job():
    print("Running scheduled email job...")
    emailer = EmailAutomation()
    emailer.send_email(
        "nanciesuresh@gmail.com",
        "Scheduled Email",
        "This is a scheduled test email."
    )


if __name__ == "__main__":
    schedule.every(1).minutes.do(job)

    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)
