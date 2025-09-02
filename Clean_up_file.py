# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:25:24 2025

@author: beckylin
"""
import os
import shutil
from datetime import datetime, timedelta

# Constants
FOLDER_PATH = "/home/pi/Documents"
TIME_THRESHOLD_DAYS = 1

def is_valid_date_folder(name):
    """Check if folder name is in YYYYMMDD format and represents a valid date."""
    try:
        folder_date = datetime.strptime(name, "%Y%m%d")
        return folder_date
    except ValueError:
        return None

def delete_future_folders(folder_path, threshold_days):
    """Delete folders whose name represents a date more than threshold_hours ahead of now."""
    if not os.path.exists(folder_path):
        print(f"Folder path {folder_path} does not exist.")
        return

    now = datetime.now()
    print(datetime.now())
    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folder_date = is_valid_date_folder(item)
            if folder_date:
                time_diff = now - folder_date
                if time_diff > timedelta(days=threshold_days):
                    try:
                        shutil.rmtree(item_path)
                        print(f" Deleted past folder: {item_path}")
                    except Exception as e:
                        print(f"Failed to delete folder {item_path}: {e}")
                else:
                    print(f"Folder {item} is within threshold.")
            #else:
                #print(f"Skipped non-date folder: {item}")

# Run the cleanup
delete_future_folders(FOLDER_PATH, TIME_THRESHOLD_DAYS)
