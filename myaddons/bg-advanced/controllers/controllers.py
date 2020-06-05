# -*- coding: utf-8 -*-
from odoo import http

# class Bg-advanced(http.Controller):
#     @http.route('/bg-advanced/bg-advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bg-advanced/bg-advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bg-advanced.listing', {
#             'root': '/bg-advanced/bg-advanced',
#             'objects': http.request.env['bg-advanced.bg-advanced'].search([]),
#         })

#     @http.route('/bg-advanced/bg-advanced/objects/<model("bg-advanced.bg-advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bg-advanced.object', {
#             'object': obj
#         })