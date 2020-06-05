# -*- coding: utf-8 -*-
from odoo import http
from .. import models
from . import controllers


class Books(http.Controller):

    @http.route('/library/books', auth='user')
    def list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([])
        return http.request.render(
            'library.book_list_template', {'books': books})
