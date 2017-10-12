#! python3
# emailCollector.py - Scrapes a web page for email addresses and saves them in a text file, then sends emails to all
# addresses it found.
# NOTE: this script is for educational purposes only, not for illegal activity. I have created this script because I
# am curious about the techniques of spammers in order to counter them; creating this script has been
# an exercise in theory and implementation.


import requests
import bs4
# import re
import smtplib
from emailCollector_config import login_credentials

# downloads the page and stores data in a variable
res = requests.get('http://www.jsc.edu/academics/mathematics/our-people/mathematics-department/')
res.raise_for_status()
websiteSoup = bs4.BeautifulSoup(res.text, "lxml")


# harvest emails from a website - what if there is display:none or js stuff to prevent spam?
emails = []
mailtos = websiteSoup.select('a[href^=mailto]')
for i in mailtos:
    if i.string is not None:
        emails.append(i.string.strip())


# TODO: collect all links on given web page
# TODO: move to next item in links list, repeat harvest
# TODO: stop web crawling after x many pages
# links = []
# http = websiteSoup.select('a[href^=http://]')
# for j in http:
#     # if j does not have a tld (.com, .org, .net, .edu, etc) discard it
#     containsTdl = re.compile(r'$\.[a-zA-Z]{2,6}')
#     mo = containsTdl.search(j)
#     if mo is True:
#         links.append(j.string)
#     elif j.string is not None:
#         links.append(j.string)
# print(links)

# TODO: save emails to file
# emailCollection = open('emailCollection.txt', 'w')
# emailCollection.write('%\n' % list(emails))

# log into email account
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
print('Logging in as', login_credentials.get('address', 0))
server.login(login_credentials.get('address', 0), login_credentials.get('password', 0))
print('Log in success.')
print('\n')

# TODO: retrieve file

# TODO: send emails
for email in emails:
    content = "Subject: Whitney\nClock strikes upon the hour\nAnd the sun begins to fade\nStill enough time to " \
              "figure out\nHow to chase my blues away\nI've done alright up to now\nIt's the light of day that " \
              "shows me how\nAnd when the night falls, loneliness calls\nOh, I wanna dance with somebody\nI wanna " \
              "feel the heat with somebody\nYeah, I wanna dance with somebody\nWith somebody who loves me\nOh, I " \
              "wanna dance with somebody\nI wanna feel the heat with somebody\nYeah, I wanna dance with somebody" \
              "\nWith somebody who loves me"
    print('Sending email to %s...' % email)

    sendMailStatus = server.sendmail(login_credentials.get('address', 0), email, content)
    if sendMailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email, sendMailStatus))
    else:
        print('Success.')
server.quit()
