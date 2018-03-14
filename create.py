import web
import db

render = web.template.render('templates/', base='layout')

class Create:
    def GET(self):
        return render.create()

    def POST(self):
        # Obtiene las datos del cliente
        data = web.input()

        # Extrae los datos recibidos
        identificador, descripcion = int(data.identificador), data.descripcion
        
        # Crea el item en la base de datos
        db.insert(identificador, descripcion)
        
        # Redirecciona a la pagina de lista de tareas
        raise web.seeother('/list')