#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from validate_date import validate_day, validate_month, validate_year
from rot13 import Rot13Handler
from signup import SignUpHandler, SignUpThanksHandler

import webapp2
import cgi

form = """
    <form method = "post">
        What is your birthday?
        <br>
        <label> Month
            <input type = "text" name = "month" value = "%(month)s">
        </label>
        <label> Day
            <input type = "text" name = "day" value = "%(day)s">
        </label>
        <label> Year
            <input type = "text" name = "year" value = "%(year)s">
        </label>
        <div style = "color: red">%(error)s</div>
        <input type = "submit">
    </form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error = "", month = "", day = "", year = ""):
        self.response.out.write(form % {"error": error,
                                        "month" : cgi.escape(month, quote = True),
                                        "day" : cgi.escape(day, quote = True),
                                        "year" : cgi.escape(year, quote = True),})

    def get(self):
        self.write_form()

    def post(self):
        user_m = self.request.get("month")
        user_d = self.request.get("day")
        user_y = self.request.get("year")
        month = validate_month(user_m)
        day = validate_day(user_d)
        year = validate_year(user_y)
        if month and day and year:
            self.redirect("/thanks")
        else:
            self.write_form("That doesn't look valid.  Please resubmit.",
                            month = user_m, day = user_d, year = user_y)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks that's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/rot13', Rot13Handler),
    ('/signup', SignUpHandler),
    ('/signupthanks', SignUpThanksHandler),
], debug=True)
