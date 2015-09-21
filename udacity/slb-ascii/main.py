import webapp2
import os
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainHandler(Handler):
    def render_front(self, title = "", art = "", error = ""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")

        self.render("front.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()

            self.redirect("/")
        else:
            error = "we need both a title and some artwork."
            self.render_front(title, art, error)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class BlogHandler(Handler):
    def render_blog(self, subject = "", content = "", error = "", posts = ""):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")

        self.render("blog.html", subject = subject, content = content, error = error, posts = posts)

    def get(self):
        self.render_blog()

class PostHandler(Handler):
    def render_post(self, subject = "", content = ""):
        self.render("post.html", subject = subject, content=content)

    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        self.render("post.html", subject=post.subject, content=post.content)

class NewPostHandler(Handler):
    def render_new(self, subject="", content="", error=""):
        self.render("new_post.html", subject = subject, content = content, error = error)

    def get(self):
        self.render_new()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            a = Post(subject = subject, content = content)
            a.put()
            id = a.key().id()
            self.redirect("/blog/%s" %str(id))
        else:
            error = "we need both a subject and some content."
            self.render_front(subject, content, error)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', BlogHandler),
    ('/blog/newpost', NewPostHandler),
    (r'/blog/(\d+)', PostHandler),
], debug=True)
