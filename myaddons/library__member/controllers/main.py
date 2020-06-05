from odoo import http
from myaddons.library.controllers.controllers import Books


class BookExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get('available'):
            Book = http.request.env['library.book']
            books = Book.search([('is_available', '=', True)])
            response.qcontext['books'] = books
        return response