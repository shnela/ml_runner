from threading import Thread

from flask import render_template
from flask_mail import Message

from app import app, mail


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template_name, **kwargs):
    msg = Message(subject, sender=app.config.get('MAIL_DEFAULT_SENDER'), recipients=[to])
    msg.body = render_template(f'{template_name}.txt', **kwargs)
    msg.html = render_template(f'{template_name}.html', **kwargs)
    thread = Thread(target=send_email_async, args=(app, msg))
    thread.start()
