import web
import db

render = web.template.render('templates/', base='layout')

class Delete:
    def GET(self, id):
        return render.delete(id)

    def POST(self, id):
        # Obtiene las datos del cliente
        data = web.input()
        
        # Extrae los datos recibidos
        identificador = int(data.id)
        
        # Crea el item en la base de datos
        db.delete(identificador)

        # Redirecciona a la pagina de lista de tareas
        raise web.seeother('/list')