# -*- coding: utf-8 -*-
from model.mail import Mail


def test_send_mail(app):
    app.session.login(username="katieden", password="rjnktnrf.12ml")
    app.mail.send(Mail(address="katieden7@gmail.com", subject="hello2"))
    app.session.logout()



