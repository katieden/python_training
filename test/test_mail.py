# -*- coding: utf-8 -*-
import pytest
from model.mail import Mail
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_send_mail(app):
    app.session.login(username="katieden", password="rjnktnrf.12ml")
    app.send_mail(Mail(address="katieden7@gmail.com", subject="hello2"))
    app.session.logout()



