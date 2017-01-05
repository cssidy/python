#! python3

# sending email
import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()

smtpObj.starttls()
smtpObj.login('user@example.com', 'password')

smtpObj.sendmail('user@example.com', 'send@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all '
                                                         'the fish,. Sincerely, Bob')
smtpObj.quit()