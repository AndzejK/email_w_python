import yagmail 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import smtplib
my_email=os.getenv("email")
password=os.getenv("password")
to_email="andzejkrupoves@gmail.com" 
subject="Nice e-mail [HTML]"
"""
The "MIME" in MIMEMultipart stands for Multipurpose Internet Mail Extensions, 
which is a standard for formatting email messages that contain multimedia content.
MIMEMultipart is useful when you want to send an email with more than just simple text. 
For example, if you want to include an image or a document, you can create a MIMEMultipart message that includes the text and the attachment(s).
"""
# Initial set-up: Building our email - the message object
message=MIMEMultipart()
message['From']=my_email
message['To']=to_email
message['Subject']=subject

# add the text part
body="""
<h2>Hey mate!</h2>
This is the day to make big decisions and live your life to the fullest potential!
"""
minetxt=MIMEText(body,'html')
message.attach(minetxt)
content=message.as_string()
print(content)

# add the image part
with open("python_language_80Mp0DHBKDy3Oms8WCM5_7.jpg", "rb") as f:
    part2 = MIMEImage(f.read())
    part2.add_header('Content-Disposition', 'attachment', filename="python_language_80Mp0DHBKDy3Oms8WCM5_7.jpg")
    message.attach(part2)

# send the email via  Gmail's SMTP server.
# server=smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(my_email, password)
# server.sendmail(my_email, to_email, content)
# server.quit()
# print("E-mail was sent")

# Using yagmail I received the image!
yag=yagmail.SMTP(user=my_email, password=password)
yag.send(to=to_email, subject=subject, contents=[body, "python_language_80Mp0DHBKDy3Oms8WCM5_7.jpg"])
print("E-mail was sent")