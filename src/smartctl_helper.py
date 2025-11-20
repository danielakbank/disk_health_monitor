import subprocess

def run_smartctl(drive_path):
    try:
        result = subprocess.run(
            ["smartctl", "-a", "-d", "sat", drive_path],  # -d sat added
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"ERROR: {e}"
