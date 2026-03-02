🚀 Comprehensive Automation Suite
📌 Project Overview

The Comprehensive Automation Suite is a modular, end-to-end Python automation framework that integrates file management, web scraping, email automation, system monitoring, task scheduling, workflow chaining, and a GUI interface into a single unified system.

This project demonstrates real-world automation architecture with modular design, configuration-driven execution, structured logging, workflow orchestration, and GUI control.

🧠 System Architecture
GUI (Tkinter)
      ↓
Workflow Designer
      ↓
Task Scheduler (JSON-based)
      ↓
Core Modules:
  - File Organizer
  - Web Scraper
  - Email Automation
  - System Monitor
      ↓
Logging & Reports
📂 Project Structure
automation_suite/
│
├── modules/
│   ├── file_organizer.py
│   ├── web_scraper.py
│   ├── email_automation.py
│   ├── system_monitor.py
│   ├── task_scheduler.py
│   └── workflow_designer.py
│
├── gui/
│   └── gui.py
│
├── configs/
│   ├── schedules.json
│   └── workflows.json
│
├── logs/
│   ├── automation_suite.log
│   └── system_report.txt
│
├── templates/
├── docs/
├── examples/
│
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone Repository
git clone <your-repository-url>
cd automation-suite
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶ How to Run
File Organizer
python -m automation_suite.modules.file_organizer
Web Scraper
python -m automation_suite.modules.web_scraper
Email Automation
python -m automation_suite.modules.email_automation
System Monitor
python -m automation_suite.modules.system_monitor
Task Scheduler
python -m automation_suite.modules.task_scheduler
Workflow Designer
python -m automation_suite.modules.workflow_designer
GUI Interface
python -m automation_suite.gui.gui
🧩 Modules Included
📁 File Organizer

Real-time folder monitoring

Automatic file categorization

Duplicate handling

Configurable categories

Logging and stats tracking

🌐 Web Scraper

Requests + BeautifulSoup

User-agent rotation

Rate limiting

JSON & CSV export

Error handling and logging

📧 Email Automation

SMTP integration

HTML email support

Template placeholders

Email scheduling

Logging of sent emails

📊 System Monitor

CPU, Memory, Disk, Network monitoring

Alert thresholds

Report generation

Logging of system stats

⏰ Task Scheduler

JSON-based task configuration

Recurring task execution

Integration with all modules

Background execution

🔗 Workflow Designer

Chain multiple modules

Load/save workflows in JSON

Step-by-step execution logging

🖥 GUI Interface

Run modules via buttons

Start/Stop scheduler

Execute workflows

Real-time status updates

Multi-threaded execution

👨‍💻 Author

Likith avala
