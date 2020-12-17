

def test_del_mail(app):
    app.session.login(username="katieden", password="rjnktnrf.12ml")
    app.mail.delete()
    app.session.logout()