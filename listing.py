import web
import db

t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates/', base='layout', globals=t_globals)

class Listing:
    def GET(self):
        items = db.listing()
        return render.list(items)  