import psutil
import time
import datetime
import logging
from automation_suite.utils import setup_logging
from automation_suite.modules.email_automation import EmailAutomation

setup_logging()


class SystemMonitor:

    def __init__(self):
        self.cpu_threshold = 80
        self.memory_threshold = 90
        self.disk_threshold = 95

    def get_system_stats(self):
        stats = {}

        stats["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stats["cpu"] = psutil.cpu_percent(interval=1)
        stats["memory"] = psutil.virtual_memory().percent
        stats["disk"] = psutil.disk_usage("/").percent

        net = psutil.net_io_counters()
        stats["network_sent"] = net.bytes_sent
        stats["network_received"] = net.bytes_recv

        logging.info("System stats collected successfully")

        return stats

    def display_stats(self):
        stats = self.get_system_stats()

        print("\n=== SYSTEM MONITOR REPORT ===")
        print(f"Timestamp       : {stats['timestamp']}")
        print(f"CPU Usage       : {stats['cpu']}%")
        print(f"Memory Usage    : {stats['memory']}%")
        print(f"Disk Usage      : {stats['disk']}%")
        print(f"Network Sent    : {stats['network_sent']} bytes")
        print(f"Network Received: {stats['network_received']} bytes")
        print("=============================\n")

        alerts = self.check_alerts(stats)

        if alerts:
            print("\n⚠ ALERT DETECTED!")
            for alert in alerts:
                print(alert)

            try:
                emailer = EmailAutomation()
                subject = "🚨 System Alert Triggered"
                body = "\n".join(alerts)

                # 🔴 PUT YOUR REAL EMAIL BELOW
                emailer.send_email("likhithaavala9@gmail.com", subject, body)

                print("Alert email sent successfully!")
                logging.info("Alert email sent successfully.")
            except Exception as e:
                print("Failed to send alert email:", e)
                logging.error(f"Failed to send alert email: {e}")

        self.save_report(stats)


    def check_alerts(self, stats):
        cpu_threshold = self.cpu_threshold
        memory_threshold = self.memory_threshold
        disk_threshold = self.disk_threshold

        alerts = []

        if stats["cpu"] > cpu_threshold:
            alerts.append(f"High CPU Usage: {stats['cpu']}%")

        if stats["memory"] > memory_threshold:
            alerts.append(f"High Memory Usage: {stats['memory']}%")

        if stats["disk"] > disk_threshold:
            alerts.append(f"High Disk Usage: {stats['disk']}%")

        if alerts:
            print("\n⚠ ALERT DETECTED ⚠")
            for alert in alerts:
                print(alert)

            # Send Email Alert
            emailer = EmailAutomation()
            subject = "System Alert - Automation Suite"
            body = "\n".join(alerts)
            emailer.send_email("nanciesuresh@gmail.com", subject, body)

        return alerts

    def save_report(self, stats):
        with open("automation_suite/logs/system_report.txt", "a") as f:
            f.write("\n=== SYSTEM REPORT ===\n")
            f.write(f"Timestamp       : {stats['timestamp']}\n")
            f.write(f"CPU Usage       : {stats['cpu']}%\n")
            f.write(f"Memory Usage    : {stats['memory']}%\n")
            f.write(f"Disk Usage      : {stats['disk']}%\n")
            f.write(f"Network Sent    : {stats['network_sent']} bytes\n")
            f.write(f"Network Received: {stats['network_received']} bytes\n")
            f.write("======================\n")


if __name__ == "__main__":
    monitor = SystemMonitor()

    try:
        while True:
            monitor.display_stats()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
