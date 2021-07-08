# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleTalgat(http.Controller):
#     @http.route('/module_talgat/module_talgat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_talgat/module_talgat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_talgat.listing', {
#             'root': '/module_talgat/module_talgat',
#             'objects': http.request.env['module_talgat.module_talgat'].search([]),
#         })

#     @http.route('/module_talgat/module_talgat/objects/<model("module_talgat.module_talgat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_talgat.object', {
#             'object': obj
#         })
