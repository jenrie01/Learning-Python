import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jenrie Merano'
email['to'] = 'andrei@zerotomastery.io', 'jenriemerano@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':  'Andrei'}), 'html')
# name = andrei

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'pass')
    smtp.send_message(email)
    print('Email sent!')

# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path

# html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'Andrei Neagoie'
# email['to'] = '<to email address>
# email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content(html.substitute({'name': 'TinTin'}), 'html')

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#   smtp.ehlo()
#   smtp.starttls()
#   smtp.login('<your email address>', '<your password>')
#   smtp.send_message(email)
#   print('all good boss!')
