import yagmail 
import os
import pandas # is a powerful tool for data analysis and we can load data from a variety of sources (e.g. CSV, Excel, SQL databases) 
my_email=os.getenv("email")
password=os.getenv("password")
subject="Contacts from a csv file"

df=pandas.read_csv('contacts.csv')
# sending email settings from WHOM
yag=yagmail.SMTP(user=my_email,password=password)

# Create a function that generates files/attachments
def generate_attch(attachment_name,content):
    with open(attachment_name,"w") as file: # here we create a file and name it too
        file.write(str(content))

for index,row in df.iterrows(): # iterrows() - it allows me to iterate over the rows of a DataFrame and access the values of each cell in the row.
    # we're going to create files
    name=row['name']
    amount=row['amount']
    receiver=row['email']
    file_name=name+'.txt'
    generate_attch(file_name,amount) # file name -> name, firstly we create a file
    dynamic_content=[f"""
    Hey {name},\nYour bill for this month is {amount}
    """,file_name] # a variable of the file name where we have create a new file for this user
    # sending the emails from .cvs file 
    yag.send(to=receiver,subject=subject,contents=dynamic_content)
    print("E-mail was sent")
