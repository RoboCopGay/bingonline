import smtplib
from email.mime.text import MIMEText
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart

from itsdangerous import URLSafeTimedSerializer
from flask import Flask, url_for, render_template


SECRET_KEY = 'my_secret_key'
SALT = 'my_password_salt'
MAIL_SERVER = 'smtp.gmail.com:587'


def generate_confirmation_token(data):
    serializer = URLSafeTimedSerializer( SECRET_KEY )
    return serializer.dumps(data, salt=SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer( SECRET_KEY )
    try:
        result = serializer.loads(token, salt=SALT, max_age=expiration)
    except:
        return False

    return result


def check_email_validation(email):
    # valid = validate_email(email, verify=True)
    # verify option is for checking if that email exists
    # default is False
    # default just examine wether the input email format is correct

    valid = validate_email(email)
    return valid


def send_mail(email, template):
    from yaml import safe_load as yml
    config = yml(open('email.yml').read())

    password = config['password']
    _from = config['email']
    _to  = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = template["subject"]
    msg['From'] = _from
    msg['To'] = _to

    msg.attach(MIMEText(template['text'], 'plain'))
    msg.attach(MIMEText(template['html'], 'html'))

    server = smtplib.SMTP( MAIL_SERVER )
    server.ehlo()
    server.starttls()
    server.login(_from,password)
    server.sendmail(_from, _to, msg.as_string())
    server.quit()
    return


def send_confirmation_mail(data):

    token = generate_confirmation_token(data)
    text = f'''
Hi {data['name']}!

Click in this link to activate your account on "{url_for('index', _external=True)}":
{url_for('index', _external=True)}user/?email_token={token}

Thank you!
    '''.strip()
    html = f'''
<h1>Hi {data['name']}</h1>
<br/>
<p>click in this link to activate your account on "<a href="{url_for('index', _external=True)}">bingonline</a>"</a>:
<p><a id='button' href="{url_for('index', _external=True)}user/?email_token={token}"><strong>Activate</strong></a></p>
<br/>
<p>Thank you!</p>
    '''.strip()

    send_mail(data['email'], {
        'subject': 'Confirm your email to create the account',
        'text': text,
        'html': html
    })
    return 

