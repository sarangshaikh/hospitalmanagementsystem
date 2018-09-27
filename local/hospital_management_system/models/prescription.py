from odoo import models,fields
class Prescription(models.Model):
	_name = 'hospitalmanagementsystem.prescription'

	name = fields.Char(string="Patient Id")
	partner_id= fields.Many2one('res.partner', string="Patient name")