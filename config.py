import web

db = web.database(dbn='sqlite', db='tasks.db')
cache = False