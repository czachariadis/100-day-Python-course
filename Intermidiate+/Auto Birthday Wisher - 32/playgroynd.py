EMAIL1 = "dummyn43@gmail.com"
EMAIL2 = "dummynumero2@yahoo.com"
PASSWORD = "D1234567810" # FOR BOTH OF THE EMAILS!
APP_PASSWORD = "djzw zxwp lnpk ltyh"

# import smtplib

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user = EMAIL1, password = PASSWORD)
# connection.sendmail(from_addr = EMAIL1, to_addrs = EMAIL2, msg = "Hello there")


# import os
from email.message import EmailMessage
import ssl
import smtplib

# email_password = os.environ.get("EMAIL_PASSWORD")
subject = "Testing Python"
body = """
Congrats you did it!!!!
"""

em = EmailMessage()
em['From'] = EMAIL1
em['To'] = EMAIL2
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(EMAIL1, APP_PASSWORD)
    smtp.sendmail(EMAIL1, EMAIL2, em.as_string())