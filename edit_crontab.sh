#!/bin/bash

# Add a cron job to run the Python script daily at 1 AM
(crontab -l 2>/dev/null; echo ""; echo "# This will run the script daily at 1 AM"; echo "0 1 * * * /usr/bin/python3 /home/pi/Documents/Clean_up_file.py >> /home/pi/Documents/Delete_file.log 2>&1") | crontab -

#Add a cron job with a comment to run the Python script every 1 hours
#(crontab -l 2>/dev/null; echo ""; echo "# This will run the script every 1 hours"; echo "0 */1 * * * /usr/bin/python3 /home/pi/Documents/Clean_up_file.py >> /home/pi/Documents/Delete_file.log 2>&1") | crontab -


# Add a cron job with a comment to run the Python script every 1 minutes
# (crontab -l 2>/dev/null; echo "*/1 * * * * /usr/bin/python3 /home/pi/Documents/Clean_up_file.py >> /home/pi/Documents/Delete_file.log 2>&1") | crontab -

# Instructions for manual editing
echo "To manually edit crontab, use: crontab -e"
echo "After editing, press Ctrl + O to save the file."
echo "Press Enter to confirm the filename."
echo "Then press Ctrl + X to exit the editor."

# List current crontab jobs
echo "Current crontab jobs:"
crontab -l

# Uncomment the following line to clear all crontab jobs
# crontab -r
