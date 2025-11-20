from drive_detector import detect_drives
from smartctl_helper import run_smartctl
from hdd_health_check import parse_smart_output
from csv_exporter import save_to_csv
from batch_tester import run_batch
from color_output import green, yellow, red
import os

# ---------------------------
# Function to print terminal report
# ---------------------------
def print_report(drive, health):
    status = health["overall_health"]

    if status == "PASS":
        status_colored = green(status)
    elif status == "FAIL":
        status_colored = red(status)
    else:
        status_colored = yellow(status)

    print(f"\n---- Report for {drive} ----")
    print("Health:", status_colored)
    print("Temperature:", health["temperature"], "°C")
    print("Reallocated sectors:", health["reallocated_sectors"])
    print("Power on hours:", health["power_on_hours"])

# ---------------------------
# Main function
# ---------------------------
def main(fake_mode=True):
    """
    If fake_mode=True, uses fake drives from src/fake_drives/
    If fake_mode=False, detects real drives and runs smartctl
    """
    if fake_mode:
        print("Running in FAKE drive mode for demo/testing...")
        # Get all fake drive files
        fake_dir = os.path.join("src", "fake_drives")
        drives = [os.path.join(fake_dir, f) for f in os.listdir(fake_dir) if f.endswith(".txt")]
    else:
        print("Detecting real drives...\n")
        drives = detect_drives()

    if not drives:
        print("No drives detected.")
        return

    print("Drives found:\n", drives)
    print("\nRunning batch test...")

    results = run_batch(drives, fake_mode=fake_mode)

    for drive, health in results:
        print_report(drive, health)

        # Export to CSV
        row = {
            "Drive": os.path.basename(drive),
            "Health": health["overall_health"],
            "Temperature": health["temperature"],
            "ReallocatedSectors": health["reallocated_sectors"],
            "PowerOnHours": health["power_on_hours"]
        }
        save_to_csv(row)

# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    # Set fake_mode=True for GitHub/demo/testing
    # Set fake_mode=False to test real drives (requires admin & smartctl)
    main(fake_mode=True)
