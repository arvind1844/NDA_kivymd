import os
import random
import math
import smtplib

def generate_otp(mail):
    digits = '0123456789'
    OTP = ''
    for i in range(6):
        OTP = OTP + digits[int(math.floor(random.random()*10))]

    otp = OTP
    msg = otp

    s = smtplib.SMTP("172.20.106.28:587")
    s.ehlo()
    s.starttls()
    s.login('shotgun@xserve.stg', 'Shotgun@321')
    emailid = input('Enter your email: ')
    s.sendmail('&&&&&&&&&&&',emailid,msg)
    a = input('Enter the OTP')
    if a == OTP:
        print("Verified")
    else:
        print("Please Check your OTP again")