import yagmail 
import os
import pandas # is a powerful tool for data analysis and we can load data from a variety of sources (e.g. CSV, Excel, SQL databases) 
my_email=os.getenv("email")
password=os.getenv("password")
subject="Contacts from a csv file"

df=pandas.read_csv('contacts.csv')
# sending email settings from WHOM
yag=yagmail.SMTP(user=my_email,password=password)

for index,row in df.iterrows(): # iterrows() - it allows me to iterate over the rows of a DataFrame and access the values of each cell in the row.
    dynamic_content=[f"""
    Hey {row['name']},\nYour bill for this month is {row['amount']}
    """,row['file']]
    # sending the emails from .cvs file 
    yag.send(to=row['email'],subject=subject,contents=dynamic_content)
    print("E-mail was sent")
