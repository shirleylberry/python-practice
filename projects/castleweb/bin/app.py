import sys
import pprint

pprint.pprint(sys.path)

import web
from castleontheweb import map
# from castleontheweb.map import Player, START

urls = (
    '/', 'Index',
    '/start', 'Start',
    '/game', 'GameEngine',
)

app = web.application(urls, globals())

if web.config.get("_session") is None:
    store = web.session.DiskStore("sessions")
    session = web.session.Session(app, store, initializer = {'room' : None, 'name' : None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render("templates/", base = "layout")

class Index(object):
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input(name = None)
        player = map.Player(form.name, [])
        session.player = player
        session.room = map.START
        return render.begin(player = session.player)

# class Start(object):
#     def GET(self):
#         print session.player.name
#         print session.room
#         web.seeother("/game")

class GameEngine(object):
    def GET(self):
        print session.room
        if session.room:
            return render.show_room(room = session.room, player = session.player)
        else:
            return render.you_died()

    def POST(self):
        form = web.input(action = None)
        if session.room and form.action:
            session.room = session.room.go(form.action)
        return render.show_room(room = session.room, player = session.player)


if __name__ == "__main__":
    app.run()