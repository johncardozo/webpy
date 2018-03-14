import config

def listing():
    return config.db.select('items')

def insert(identificador, descripcion):
    config.db.insert('items', id=identificador, author_id=identificador, body=descripcion)

def delete(identificador):
    config.db.delete('items', where='id=' + str(identificador))    