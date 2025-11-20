import csv
import os
from utils.file_paths import CSV_EXPORT_PATH

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_EXPORT_PATH)

    with open(CSV_EXPORT_PATH, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow(data.keys())  # write header

        writer.writerow(data.values())
