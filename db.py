import config

def listing():
    return config.db.select('items')