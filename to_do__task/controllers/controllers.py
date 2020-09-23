# -*- coding: utf-8 -*-
from odoo import http

# class ToDoTask(http.Controller):
#     @http.route('/to_do__task/to_do__task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to_do__task/to_do__task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('to_do__task.listing', {
#             'root': '/to_do__task/to_do__task',
#             'objects': http.request.env['to_do__task.to_do__task'].search([]),
#         })

#     @http.route('/to_do__task/to_do__task/objects/<model("to_do__task.to_do__task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to_do__task.object', {
#             'object': obj
#         })