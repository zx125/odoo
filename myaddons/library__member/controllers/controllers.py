# -*- coding: utf-8 -*-
from odoo import http

# class LibraryMember(http.Controller):
#     @http.route('/library__member/library__member/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library__member/library__member/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library__member.listing', {
#             'root': '/library__member/library__member',
#             'objects': http.request.env['library__member.library__member'].search([]),
#         })

#     @http.route('/library__member/library__member/objects/<model("library__member.library__member"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library__member.object', {
#             'object': obj
#         })