import psutil
import platform

def detect_drives():
    system = platform.system().lower()
    drives = []

    if system == "windows":
        # Windows uses PhysicalDrive0, 1, etc.
        for i in range(10):
            drives.append(f"\\\\.\\PhysicalDrive{i}")

    else:
        # Linux/macOS
        for disk in psutil.disk_partitions(all=True):
            if "/dev/" in disk.device:
                drives.append(disk.device)

    return list(set(drives))
