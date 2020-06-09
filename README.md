# attend

**Purpose**
The purpose of this script is to never miss an attendence check, break time or watch during bootcamp, because it's easy to lose track of time while coding

**Process**
For attendence check.
At 08h55, 10h25, 12h25, 16h55
Check if discord is open
Open discord.
Switch to general vocal channel

For the watch
At 13h25
Check if discord is open.
Switch to techtalk channel


**useful Python snippets*
import os
os.system(fileName+'.exe')

import schedule
import time

def job():
    print("I am doing this job!")

schedule.every().monday.at("14:00").do(job)
schedule.every().tuesday.at("14:00").do(job)
schedule.every().wednesday.at("14:00").do(job)
schedule.every().thursday.at("14:00").do(job)
schedule.every().friday.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
