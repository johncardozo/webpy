import web

render = web.template.render('templates/')

class Index:
    def GET(self, name):
        return render.index(name)