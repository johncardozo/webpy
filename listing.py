import web

render = web.template.render('templates/')

class Listing:
    def GET(self):
        return render.list()  