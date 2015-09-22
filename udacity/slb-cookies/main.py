import webapp2
import os
import jinja2

from google.appengine.ext import db
import hashlib

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def hash_str(s):
    return hashlib.md5(s)

def make_secure_val(s):
    return "%s,%s" %(s, hash_str(s))

def check_secure_val(h):
    orig_word = h.split(',')
    if orig_word[1] == hash_str(h[0]):
        return h[0]
    else:
        return None

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visit_cookie_str = self.request.cookies.get('visits')
        if visit_cookie_val:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)
        visits += 1

        new_cookie_val = make_secure_val(str(visits))
        self.response.headers.add_header('Set-Cookie', 'visits=%s' %visits, [])
        if visits > 100:
            self.write("You are the best ever.")
        else:
            self.write("you've been here %s times" % str(visits))

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
