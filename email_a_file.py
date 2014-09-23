
## sending an email

import time
import smtplib
from email.mime.text import MIMEText

# smpt_host = 'smtp.live.com'
smtp_host = 'smtp.gmail.com'
# smpt_host = 'smtp.mail.yahoo.com


#  textfile is the name of the program

fp = open('email_a_file.py', 'rb')

# create a plain text message

msg = MIMEText(fp.read())
fp.close()




msg['Subject'] = 'email_a_file.py'



mail = smtplib.SMTP(smtp_host,587,timeout=10)

mail.set_debuglevel(1)

mail.ehlo()

mail.starttls()

mail.ehlo()

mail.login('dxjones00','that password')

mail.sendmail('dxjones00@gmail.com','dxjones00@yahoo.com', msg.as_string())

mail.quit()


