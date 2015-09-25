import webapp2
import cgi
import string
import re
import os
import hashlib, hmac
import random

import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

secret = "1234DJFKJSDF"

def hash_str(s):
    return hmac.new(secret, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" %(s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val



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

    def verify_username(self, username):
        username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username_re.match(username)

    def verify_password(self, password):
        password_re = re.compile(r"^.{3,20}$")
        return password_re.match(password)

    def verify_email(self, email):
        email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        return email_re.match(email)

    def get(self):
        self.render_new()

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        v_username = self.verify_username(username)
        v_password = self.verify_password(password)
        v_email = self.verify_email(email)
        if password != verify:
            error = "The two passwords don't match.  Please try again."
            self.render_new(username, email, error)
        elif v_username and v_password and v_email:
            cookie_val = make_secure_val(username)
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
        username = self.request.cookies.get('username')
        if username:
            name = make_secure_val(username)
            if check_secure_val(name):
                self.render_new(username=username)
            else:
                self.redirect("/signup")
