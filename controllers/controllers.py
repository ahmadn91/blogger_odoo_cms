# -*- coding: utf-8 -*-
# from odoo import http


# class BloggerOdooCms(http.Controller):
#     @http.route('/blogger_odoo_cms/blogger_odoo_cms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blogger_odoo_cms/blogger_odoo_cms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blogger_odoo_cms.listing', {
#             'root': '/blogger_odoo_cms/blogger_odoo_cms',
#             'objects': http.request.env['blogger_odoo_cms.blogger_odoo_cms'].search([]),
#         })

#     @http.route('/blogger_odoo_cms/blogger_odoo_cms/objects/<model("blogger_odoo_cms.blogger_odoo_cms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blogger_odoo_cms.object', {
#             'object': obj
#         })
