import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_ADDRESS = os.environ.get('EMAIL')
EMAIL_PASSWORD = os.environ.get('PASSWORD')

# print(EMAIL_ADDRESS)
# print(EMAIL_PASSWORD)

while True:
    def send_goal_mails():
        r = requests.get('https://www.goal.com').text

        headings = ''

        soup = BeautifulSoup(r, 'lxml')
        for table_data in soup.find_all('td', class_="widget-news-card__content"):
            headline = table_data.h3.a.text
            headings += headline+'\n\n'

        with open('goal_news.txt', 'w') as f:
            f.write(headings)

        try:
            msg = EmailMessage()
            msg['Subject'] = 'Goal Websites News Headlines:'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = 'tundemuhamed@gmail.com'
            msg.set_content('File attached...')

            file = 'goal_news.txt'
            with open(file, 'r') as bf:
                file_data = bf.read()
                file_name = bf.name
            msg.add_attachment(file_data, filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

        except smtplib.SMTPResponseException:
            pass

    send_goal_mails()

    # send mail after 2 minutes
    time.sleep(5)
