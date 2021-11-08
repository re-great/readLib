import smtplib
import os
from email.message import EmailMessage
import secrets
from sqlite3.dbapi2 import Connection, connect


def get_otp(lim):
    return secrets.token_urlsafe()[:lim]

PROJ_EMAIL = ''
PROJ_PASS = ''




def otp_email(receiver,lim=8):
    otp = get_otp(lim)

    with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465 ) as smtp:
        try:
            msg = EmailMessage()

            if lim == 8:
                msg['Subject'] = 'Password Reset OTP'
                msg.set_content(f"{otp} is password reset your OTP for Username {receiver[0]}")
            if lim == 6:
                msg['Subject'] = 'Verify Your Email now'
                msg.set_content(f"{otp} is Your OTP for Email verification")
            msg['From'] = PROJ_EMAIL
            msg['To'] = str(receiver[2])
            
            smtp.login(PROJ_EMAIL , PROJ_PASS)
            smtp.send_message(msg)
            print(msg)
            smtp.quit()
        # except SMTPRecipientsRefused:
        #     print("INVALID EMAIL")
        #     return '!'*lim 
        except :
            print('INAVLID 2')
            return '!'*lim
    print(otp)
    return otp








