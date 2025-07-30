##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


from email.message import EmailMessage
import ssl
import smtplib
import datetime as dt
import pandas as pd


EMAIL1 = "dummyn43@gmail.com"
EMAIL2 = "dummynumero2@yahoo.com"
PASSWORD = "D1234567810" # FOR BOTH OF THE EMAILS!
APP_PASSWORD = "djzw zxwp lnpk ltyh"


# Get datetime
current_datetime = dt.datetime.now()
month = current_datetime.month
day = current_datetime.day

# Get Birthdays
df = pd.read_csv("birthdays.csv")
names = df["names"]
emails = ["emails"]
birthdates = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)