import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "../../logs/")
SMART_REPORT_DIR = os.path.join(LOG_DIR, "smart_reports/")
CSV_EXPORT_PATH = os.path.join(BASE_DIR, "../../exports/drive_health.csv")

# Create folders if missing
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SMART_REPORT_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "../../exports/"), exist_ok=True)
