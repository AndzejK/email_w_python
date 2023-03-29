import yagmail 
import os
my_email=os.getenv("email")
password=os.getenv("password")
to_email="#" # https://10minutemail.net
subject="Testing my email-python-skills"
content=["""
Hey <b>Mate</b>,
How doing?
""","contacts.csv"] # we just need to modify content, as list and second value will be the path of the file
# sending email settings from WHOM
yag=yagmail.SMTP(user=my_email,password=password)
# sending email settings to WHOM
yag.send(to=to_email,subject=subject,contents=content)
print("E-mail was sent")
