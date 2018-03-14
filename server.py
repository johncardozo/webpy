import web
from item import Item
from listing import Listing
from index import Index

urls = (
    '/', 'Index',
    '/list', 'Listing',
    '/item', 'Item'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()