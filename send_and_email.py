import yagmail 
import os
my_email=os.getenv("email")
password=os.getenv("password")
to_email="vmn26054@zslsz.com" # https://10minutemail.net
subject="Testing my email-python-skills"
content="""
Hey <b>Mate</b>,
How doing?
"""
# sending email settings from WHOM
yag=yagmail.SMTP(user=my_email,password=password)
# sending email settings to WHOM
yag.send(to=to_email,subject=subject,contents=content)
print("E-mail was sent")
