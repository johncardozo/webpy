import config

def listing():
    return config.db.select('items')

def insert(identificador, descripcion):
    config.db.insert('items', id=identificador, author_id=identificador, body=descripcion)