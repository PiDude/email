
## sending an email

import time
import smtplib

# smpt_host = 'smtp.live.com'
smtp_host = 'smtp.gmail.com'
# smpt_host = 'smtp.mail.yahoo.com'

subject = 'Python Test'

email_body = "this is the body of a test email-1"

mail = smtplib.SMTP(smtp_host,587,timeout=10)

mail.set_debuglevel(1)

mail.ehlo()

mail.starttls()

mail.ehlo()

mail.login('dxjones00','GOOGpwd1')

mail.sendmail('dxjones00@gmail.com','dxjones00@yahoo.com',email_body)

mail.quit()


