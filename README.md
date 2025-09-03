# Crontab-Task-Scheduler-in-Linux
Crontab (short for "cron table") is a powerful time-based job scheduler in Unix-like operating systems, including Linux. It allows users to automate repetitive tasks by scheduling scripts or commands to run at specific times or intervals.
# How does it work
```
*  *  *  *  *  *
-  -  -  -  -  -
|  |  |  |  |  + year [optional]
|  |  |  |  +----- day of week (0 - 7) (Sunday=0 or 7)
|  |  |  +---------- month (1 - 12)
|  |  +--------------- day of month (1 - 31)
|  +---------------------- hour (0 - 23)
+----------------------------- min (0 - 59)
```
# Linux_Environment
Edit crontab content
```
crontab -e
```
Add the following script for task scheduler
```
# For 5hr
0 */5 * * * /usr/bin/python3 /home/pi/Documents/Clean_up_file.py >> /home/pi/Documents/check.log 2>&1

# For 3min
#*/3 * * * * /usr/bin/python3 /home/pi/Documents/Clean_up_file.py >> /home/pi/Documents/check.log 2>&1
```
After editing, press ```Ctrl + O``` to save the file.

Press ```Enter``` to confirm the filename.

Then press ```Ctrl + X``` to exit the editor.

Check the crontab content
```
crontab -l
```
Clear All Crontab Jobs
```
crontab -r
```
