import config

def listing():
    return config.db.select('items')

def insert(descripcion, tiempo):
    config.db.insert('items', estimated_time=tiempo, body=descripcion)

def delete(identificador):
    config.db.delete('items', where='id=' + str(identificador))    