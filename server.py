import web
from item import Item
from listing import Listing
from index import Index
from createdb import CreateDB

urls = (
    '/list', 'Listing',
    '/item', 'Item',
    '/(.*)', 'Index'    
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()