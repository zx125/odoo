# -*- coding: utf-8 -*-
from odoo import http

# class BugManage(http.Controller):
#     @http.route('/bug_manage/bug_manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug_manage/bug_manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug_manage.listing', {
#             'root': '/bug_manage/bug_manage',
#             'objects': http.request.env['bug_manage.bug_manage'].search([]),
#         })

#     @http.route('/bug_manage/bug_manage/objects/<model("bug_manage.bug_manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug_manage.object', {
#             'object': obj
#         })
class Bug(http.Controller):
    @http.route('/bug-manage')
    def BugManage(self,**kwargs):
        bugs=http.request.env['bm.bug']
        domain_bug=[('is_closed','=',False)]
        bugs_open=bugs.search(domain_bug)
        return http.request.render('bug_manage.bugs_template',{'bugs_open':bugs_open})