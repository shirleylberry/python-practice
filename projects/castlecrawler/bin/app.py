import web

urls = (
    '/', 'Index',
    '/hello', 'HelloForm',
)

app = web.application(urls, globals())
render = web.template.render("templates/", base = "layout")


class Index(object):
    def GET(self):
        return render.index(greeting = "Hello")

class HelloForm(object):
    def GET(self):
        greeting = "Hello nobody"
        return render.hello_form(greeting)
    def POST(self):
        form = web.input(greet = "Hello", name = "nobody")
        greeting = "%s %s" %(form.greet, form.name)
        if form.greet:
            return render.hello_form(greeting)


if __name__ == "__main__":
    app.run()