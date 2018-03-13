import web

render = web.template.render('templates/')

class Item:
    def GET(self):
        return render.item() 