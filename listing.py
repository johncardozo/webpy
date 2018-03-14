import web
import db

render = web.template.render('templates/', base='layout')

class Listing:
    def GET(self):
        items = db.listing()
        return render.list(items)  