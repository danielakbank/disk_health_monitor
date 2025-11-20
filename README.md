# HDD/SSD SMART Diagnostic Tool 🖤️🔦

A **lightweight Python tool** that automates **drive health monitoring** using SMART attributes.  
Designed to simulate **warehouse-grade HDD/SSD testing workflows**, process multiple drives, and generate **color-coded terminal reports, logs, and CSV summaries**. Perfect for demonstrating **hardware diagnostics, batch testing, and workflow automation**.

---

## Features ✨

- **Batch Drive Testing** – Test multiple drives at once (real or simulated).  
- **SMART Attribute Parsing** – Extracts key indicators:  
  - Health status (PASS / WARNING / FAIL)  
  - Temperature (°C)  
  - Reallocated sectors  
  - Power-on hours  
- **Color-coded Terminal Output** – Green = PASS, Yellow = WARNING, Red = FAIL.  
- **CSV Export & Logs** – Maintain a record of all drive tests for reporting or QA.  
- **Fake Drive Simulation Mode** – Test your workflow without real drives (perfect for demos or GitHub portfolios).  

---

## Installation ⚙️

1. Clone the repository:

```bash
git clone https://github.com/danielakbank/disk_health_monitor.git
cd disk_health_monitor
```

2. Create a virtual environment (recommended):

```bash
python -m venv .venv
```

3. Activate the environment:

- **Windows:**

```bash
.venv\Scripts\activate
```

- **Linux/Mac:**

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage 🏃🏻‍♂️

### Run with **fake drives** (recommended for demo/portfolio)

```bash
python src/main.py
```

- Reads all files in `src/fake_drives/`  
- Generates terminal report, CSV in `exports/`, and logs in `logs/`  

### Run with **real drives**

Edit `main.py` to:

```python
main(fake_mode=False)
```

- Detects all connected drives using `smartctl`  
- Requires **smartmontools** installed and admin privileges  

---

## Example Output 🎟️

**Terminal:**

```
---- Drive: fake_drive1.txt ----
Health: PASS
Temperature: 41 °C
Reallocated sectors: 0
Power on hours: 1200

---- Drive: fake_drive2.txt ----
Health: WARNING
Temperature: 55 °C
Reallocated sectors: 5
Power on hours: 2500

---- Drive: fake_drive3.txt ----
Health: FAIL
Temperature: 70 °C
Reallocated sectors: 15
Power on hours: 5000
```

**CSV Summary (`exports/drive_health.csv`):**

```
Drive,Health,Temperature,ReallocatedSectors,PowerOnHours
fake_drive1.txt,PASS,41,0,1200
fake_drive2.txt,WARNING,55,5,2500
fake_drive3.txt,FAIL,70,15,5000
```

---

## Project Structure 🏷️

```
disk_health_monitor/
│
├─ src/
│  ├─ main.py              # Entry point
│  ├─ drive_detector.py    # Detects connected drives
│  ├─ smartctl_helper.py   # Runs smartctl and returns raw SMART data
│  ├─ hdd_health_check.py  # Parses SMART output
│  ├─ csv_exporter.py      # Exports data to CSV
│  ├─ color_output.py      # Color-coded terminal output
│  ├─ batch_tester.py      # Handles batch testing of drives
│  └─ fake_drives/         # Fake SMART files for testing/demo
│
├─ logs/                   # Stores raw SMART reports
├─ exports/                # Stores CSV summaries
├─ README.md
└─ requirements.txt
```

---

## Why This Project Is Relevant 💡

- **Simulates high-volume drive testing workflows** – like those in ITAD and warehouse environments.  
- **Shows problem-solving and automation skills** – batch testing multiple drives efficiently.  
- **Demonstrates technical knowledge** – SMART attributes, diagnostics, Linux/Windows tools.  
- **Portfolio-ready** – use it to impress hiring managers and showcase your practical skills.  

---

## Dependencies 📦

- Python 3.9+  
- [psutil](https://pypi.org/project/psutil/) – drive detection  
- [colorama](https://pypi.org/project/colorama/) – terminal colors  
- [smartmontools](https://www.smartmontools.org/) – required for real drive testing  

---

## License 📓

This project is **MIT licensed**. Feel free to use and adapt it for your portfolio or learning purposes.

---

## Author

**Daniel Akinbankole** – Portfolio project for **HDD/SSD testing & diagnostics**, demonstrating workflow automation, batch processing, and technical problem-sol