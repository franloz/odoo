# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo399(models.Model):
#     _name = 'odoo399.odoo399'
#     _description = 'odoo399.odoo399'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class zapatilla399(models.Model):
	_name = 'odoo399.zapatilla399'
	_description = 'model zapatilla399'

	name = fields.Char('Id',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)
