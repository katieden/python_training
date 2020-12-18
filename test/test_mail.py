# -*- coding: utf-8 -*-
from model.mail import Mail


def test_send_mail(app):
    app.mail.send(Mail(address="katieden7@gmail.com", subject="hello2"))



