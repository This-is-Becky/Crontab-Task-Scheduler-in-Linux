# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:19:50 2023

@author: beckylin
"""

import os
import subprocess
from datetime import datetime, timedelta
import time

# Constants
#FOLDER_PATH = './Vid'
FOLDER_PATH = '/home/pi/Downloads/Vid'
TIME_THRESHOLD_HOURS = 2

def get_today_folder():
    return os.path.join(FOLDER_PATH, datetime.today().strftime('%Y%m%d'))

def extract_timestamp_from_filename(filename):
    try:
        # Filename format: Vid_YYYYMMDD_HHMMSSffffff.mp4
        base = os.path.basename(filename)
        timestamp_str = base.split('_')[1] + '_' + base.split('_')[2].split('.')[0]
        return datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S%f')
    except Exception as e:
        print(f"Error extracting timestamp: {e}")
        return None

def check_last_record_time():
    today_folder = get_today_folder()
    print("delay30sec")
    time.sleep(30)
    print(datetime.today())

    # If today's folder doesn't exist, search previous folders
    if not os.path.exists(today_folder):
        print("Today's folder does not exist. Searching previous folders...")
        

        # Find the most recent folder with .wav files
        folders = sorted(
            [f for f in os.listdir(FOLDER_PATH) if os.path.isdir(os.path.join(FOLDER_PATH, f))],
            reverse=True
        )

        folder = None
        for f in folders:
            folder_path = os.path.join(FOLDER_PATH, f)
            vid_files = [vd for vd in os.listdir(folder_path) if vd.endswith('.mp4')]
            if vid_files:
                folder = folder_path
                break

        if not folder:
            print("No valid folders with .mp4 files found.")
            return
    else:
        folder = today_folder

    # Find the latest .mp4 file in the selected folder
    mp4_files = [f for f in os.listdir(folder) if f.endswith('.mp4')]
    if not vid_files:
        print("No .mp4 files found in the selected folder.")
        return

    vid_files.sort(reverse=True)
    latest_file = vid_files[0]
    latest_file_path = os.path.join(folder, latest_file)
    print(f"Latest file found: {latest_file_path}")

    try:
        timestamp_str = latest_file.split('_')[1] + '_' + latest_file.split('_')[2].split('.')[0]
        file_time = datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S%f')
    except Exception as e:
        print(f"Error parsing timestamp: {e}")
        return

    time_diff = datetime.now() - file_time
    print(f"Time difference: {time_diff}")

    if time_diff > timedelta(hours=TIME_THRESHOLD_HOURS):
        print(f"Last record is older than {TIME_THRESHOLD_HOURS} hours. Rebooting system...")
        subprocess.call(['sudo', 'reboot'])
    else:
        print(f"Last record is within {TIME_THRESHOLD_HOURS} hours. No reboot needed.")


# Run the check
check_last_record_time()

