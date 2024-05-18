import smtplib
from email.message import EmailMessage
from credetionals import password
import ssl



email_sender= 'janghuanshika@gmail.com'
email_passowrd = password
email_receiver = 'yodane1150@rencr.com'
subject = "Follow up mail"
body = """
Hi, this an follow up mail to engage in conversation with us for better data mangement and visualization.
"""
em= EmailMessage()
em['From']= email_sender
em['To']= email_receiver
em['subject']= subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_passowrd)
    smtp.sendmail(email_sender, email_receiver, em.as_string())




