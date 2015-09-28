import re

def verify_username(username):
        username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username_re.match(username)

def verify_password(password):
    password_re = re.compile(r"^.{3,20}$")
    return password_re.match(password)

def verify_email(email):
    email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return email_re.match(email)