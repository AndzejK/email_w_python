import yagmail 
import os
import time
from datetime import datetime as dt # make shorter

structure_for_date_and_time="%Y-%m-%d_%H:%M:%S"
get_time=dt.today()
mod_str_time=get_time.strftime(structure_for_date_and_time)

while True:
    # here we have if condition when and how often we want to send an email
    now=dt.now()
    if now.hour==9 and now.minute==10: #We want to send an email every day at this time
        my_email=os.getenv("email")
        password=os.getenv("password")
        to_email="cja27784@omeie.com" # https://10minutemail.net
        subject="An email per A second"
        content="""
        Hey <b>Mate</b>,
        this is SPAM!!!
        """
        yag=yagmail.SMTP(user=my_email,password=password)
        # sending email settings from WHOM
        # sending email settings to WHOM
        yag.send(to=to_email,subject=subject,contents=content)
        print("E-mail was sent")
        time.sleep(60) # since in if CONDITION we have min thus this script will pause for one min and let's say we wanna send each hour then we need to wait for and hour :) but here 

# https://www.pythonanywhere.com/ -> where I can host python scripts and schedule scripts
#https://pythonhow.com/how/schedule-a-python-script-for-execution-at-a-specific-time-every-day/ instructions for it
