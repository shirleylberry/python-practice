from validate_date import validate_day, validate_month, validate_year
from signup import SignUpHandler, SignUpThanksHandler

import webapp2
import os
import jinja2

from google.appengine.ext import db


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignUpHandler),
    ('/welcome', SignUpThanksHandler)
], debug=True)
