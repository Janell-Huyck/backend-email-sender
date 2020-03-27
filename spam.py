#!usr/bin/env python3

"""
A tiny email program to send spam to someone
"""

import os
import smtplib

EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
# setup a gmail app password
# get the password into this program
# use the stmplib import to send email

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)

    # compose the email message
    subject = "Keep on Truckin"
    body = "Whooo @ me: keep on truckin that truck"
    msg = f"Subject: {subject}\n\n{body}"

    # do actual send
    smtp.sendmail(EMAIL_USERNAME, 'kenzie.academy@mailinator.com', msg)
