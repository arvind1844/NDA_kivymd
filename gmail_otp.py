import os
import math
import random
import smtplib


#
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[int(math.floor(random.random()*10))]
otp = OTP + ' is your otp'
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login("nda.cmpl@gmail.com", "txijbefmmrkidmzp")
emailid = input('Enter your email: ')
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")