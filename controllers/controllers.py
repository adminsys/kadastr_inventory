# -*- coding: utf-8 -*-
# from odoo import http


# class KadastrInventory(http.Controller):
#     @http.route('/kadastr_inventory/kadastr_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kadastr_inventory/kadastr_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kadastr_inventory.listing', {
#             'root': '/kadastr_inventory/kadastr_inventory',
#             'objects': http.request.env['kadastr_inventory.kadastr_inventory'].search([]),
#         })

#     @http.route('/kadastr_inventory/kadastr_inventory/objects/<model("kadastr_inventory.kadastr_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kadastr_inventory.object', {
#             'object': obj
#         })
