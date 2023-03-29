import yagmail 
import os
import time
import datetime

structure_for_date_and_time="%Y-%m-%d_%H:%M:%S"
get_time=datetime.datetime.today()
mod_str_time=get_time.strftime(structure_for_date_and_time)

while True:
    my_email=os.getenv("email")
    password=os.getenv("password")
    to_email="crm45450@nezid.com" # https://10minutemail.net
    subject="An email per A second"
    content="""
    Hey <b>Mate</b>,
    this is SPAM!!!
    """
    # sending email settings from WHOM
    yag=yagmail.SMTP(user=my_email,password=password)
    # sending email settings to WHOM
    yag.send(to=to_email,subject=subject,contents=content)
    print("E-mail was sent")
    time.sleep(60)