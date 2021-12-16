# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo399(http.Controller):
#     @http.route('/odoo399/odoo399/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo399/odoo399/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo399.listing', {
#             'root': '/odoo399/odoo399',
#             'objects': http.request.env['odoo399.odoo399'].search([]),
#         })

#     @http.route('/odoo399/odoo399/objects/<model("odoo399.odoo399"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo399.object', {
#             'object': obj
#         })
