from smartctl_helper import run_smartctl
from hdd_health_check import parse_smart_output
import os

def run_batch(drives, fake_mode=False):
    """
    drives: list of drive paths or fake drive files
    fake_mode: True if using fake SMART files
    Returns: list of tuples (drive_name, health_dict)
    """
    results = []

    for drive in drives:
        if fake_mode:
            # Read fake SMART file
            with open(drive, "r") as f:
                output = f.read()
        else:
            # Run smartctl for real drive
            output = run_smartctl(drive)

        health = parse_smart_output(output)
        results.append((drive, health))

    return results
