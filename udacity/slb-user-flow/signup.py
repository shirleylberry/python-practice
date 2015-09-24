import webapp2
import cgi
import string
import re


class SignUpHandler(webapp2.RequestHandler):
    def write_form(self, error = "", username = "", password = "", verify = "", email = ""):
        self.response.out.write(form % {"error" : error,
                                        "username" : cgi.escape(username, quote = True),
                                        "password" : cgi.escape(password, quote = True),
                                        "verify" : cgi.escape(verify, quote = True),
                                        "email" : cgi.escape(email, quote = True),})

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
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        v_username = self.verify_username(username)
        v_password = self.verify_password(password)
        v_email = self.verify_email(email)
        if password != verify:
            error = "The two passwords don't match.  Please try again."
            self.write_form(error, username, password, verify, email)
        elif v_username and v_password and v_email:
            self.redirect("/signupthanks?username=" + username)
        elif not v_username:
            error = "Please enter a valid username."
            self.write_form(error, username, password, verify, email)
        elif not v_password:
            error = "Please enter a valid password."
            self.write_form(error, username, password, verify, email)
        elif not v_email:
            error = "Please enter a valid email."
            self.write_form(error, username, password, verify, email)

class SignUpThanksHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        msg = "Welcome, %s" % username
        self.response.write(msg)
