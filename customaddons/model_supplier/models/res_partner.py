# -*- coding: utf-8 -*-
from odoo import models,fields,api


class ResPartner(models.Model):
	_inherit = 'res.partner'


	is_supplier = fields.Boolean(string="Fornecedor", default=False)



	# @api.onchange('company_type')	
	# def onchange_company_type(self):
	# 	if self.company_type == ''
