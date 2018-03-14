import web
from item import Item
from listing import Listing
from index import Index
from create import Create
from delete import Delete

urls = (
    '/', 'Index',
    '/list', 'Listing',
    '/item', 'Item',
    '/create', 'Create',
    '/delete/(\d+)', 'Delete'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()