# Crontab-Task-Scheduler-in-Linux
Crontab (short for "cron table") is a powerful time-based job scheduler in Unix-like operating systems, including Linux. 

In Linux-based systems, repetitive tasks like **file cleanup**, **system maintenance**, or **sending notification**s can be automated using cron, a time-based job scheduler. 

This project demonstrates how to leverage crontab to schedule and execute tasks automatically, reducing manual effort and improving operational efficiency.

## How does it work
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
## Python Script: `Clean_up_file.py` Function:

- Checks folder names to see if they match a valid date format.
- Compares each folder's date to the current date.
- Deletes folders older than the threshold (1 day by default).
- Logs actions and errors to the console.

## Shell Script: `edit_crontab.sh` Function:

- Run the Python script automatically with the desire schedule setting

 ## Step by step
 1. Add permission 
`chmod +x edit_crontab.sh`

2. Run the script
`./edit_crontab.sh`

