from threading import Thread

from flask import render_template, current_app
from flask_mail import Message

from app import mail


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template_name, **kwargs):
    msg = Message(subject, sender=current_app.config.get('MAIL_DEFAULT_SENDER'), recipients=[to])
    msg.body = render_template(f'{template_name}.txt', **kwargs)
    msg.html = render_template(f'{template_name}.html', **kwargs)
    thread = Thread(target=send_email_async, args=(current_app._get_current_object(), msg))
    thread.start()
