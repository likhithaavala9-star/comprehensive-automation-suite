import os

# File Organizer Categories
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.jpeg'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3'],
}

# General settings
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/automation_suite.log'

# File Organizer
WATCH_FOLDER = r"C:\Users\Likitha\Downloads"
ORGANIZED_FOLDER = r"C:\Users\Likitha\Organized"

# Web Scraper
SCRAPER_URLS = ['https://httpbin.org/html']
PROXIES = []
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
]
RATE_LIMIT = 1

# Email Automation
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'likhithaavala9@gmail.com'
EMAIL_PASS = 'atzwpfooyisojrhz'
TEMPLATES_DIR = 'templates/'

# System Monitor
MONITOR_INTERVAL = 60
ALERT_THRESHOLDS = {'cpu': 80, 'memory': 90, 'disk': 95}

# Task Scheduler
SCHEDULE_FILE = 'configs/schedules.json'

# Workflow Designer
WORKFLOW_FILE = 'configs/workflows.json'
