import webapp2
import cgi
import string
import re
import os
import hashlib, hmac
import random

import jinja2

from google.appengine.ext import db

from validate_user import verify_email, verify_password, verify_username

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

secret = "1234DJFKJSDF"

def hash_str(s):
    return hmac.new(secret, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" %(s, hash_str(s))

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty(required = False)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class SignUpHandler(Handler):
    def render_new(self, username="", email="", error=""):
        self.render("signup.html", username = username, email = email, error = error)

    def check_exists(self, username):
        # users = db.GqlQuery("SELECT * FROM User WHERE user.username=username")
        # if users:
        #     return True
        # else:
        #     return None


    def get(self):
        self.render_new()

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        v_username = verify_username(username)
        v_password = verify_password(password)
        v_email = verify_email(email)
        if password != verify:
            error = "The two passwords do not match.  Please try again."
            self.render_new(username=username, email=email, error=error)
        elif v_username and v_password and v_email:
            cookie_val = make_secure_val(username)
            if self.check_exists(username):
                error = "User already exists."
                self.render_new(username, email, error)
            else:
                u = User(username = username, pw_hash = cookie_val, email = email)
                u.put()
            self.response.headers.add_header('Set-Cookie', 'username=%s;path=/' %str(cookie_val))
            self.redirect("/welcome")
        elif not v_username:
            error = "Please enter a valid username."
            self.render_new(username, email, error)
        elif not v_password:
            error = "Please enter a valid password."
            self.render_new(username, email, error)
        elif not v_email:
            error = "Please enter a valid email."
            self.render_new(username, email, error)

class SignUpThanksHandler(Handler):
    def render_new(self, username=""):
        self.render("welcome.html", username = username)

    def get(self):
        user_cookie = self.request.cookies.get('username')
        username = user_cookie.split('|')[0]
        if user_cookie:
            valid_check = check_secure_val(user_cookie)
            if username == valid_check:
                self.render_new(username=username)
            else:
                self.redirect("/signup")
