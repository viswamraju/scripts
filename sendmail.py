"""
Python comes with the built-in smtplib module for sending emails using the Simple Mail Transfer Protocol (SMTP)

Create a gmail account
Turn ON Less secure app access


"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
password = 'Mawsiv@123'

# Create a secure SSL context
context = ssl.create_default_context()


def send_plain_message():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("viswamtest123@gmail.com", password)
        server.sendmail("viswamtest123@gmail.com", "viswamraju@gmail.com", "THis is a test message")


def send_fancy_mail():
    message = MIMEMultipart("alternative")
    message['Subject'] = "multipart test"
    message['From'] = 'viswamtest123@gmail.com'
    message['To'] = 'viswamraju@gmail.com'

    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a>
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("viswamtest123@gmail.com", password)
        server.sendmail("viswamtest123@gmail.com", "viswamraju@gmail.com", message.as_string())
    

# send_plain_message()
send_fancy_mail()
