from odoo import models,fields,api,_

class Prescription(models.Model):
	_name = 'hospitalmanagementsystem.prescription'
	prescriptionlines_id=fields.One2many('hospitalmanagementsystem.prescriptionlines','prescription_id',string="PrescriptionLines")

	name = fields.Char(string='Prescription Id', index=True,
		default=lambda self: _('New'))

	partner_id= fields.Many2one('res.partner', string="Patient name")
	doctor_id=fields.Char(string="Doctor")
	pharmacy_id=fields.Char(string="Pharmacy")
	prescription_date=fields.Date(string="Prescription Date")


	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagementsystem.prescription') or _('New')
			return super(Prescription, self).create(vals)


class PrescriptionLines(models.Model):
	_name='hospitalmanagementsystem.prescriptionlines'
	prescription_id=fields.Many2one('hospitalmanagementsystem.prescription',string="Prescription Id")
	
	medicine=fields.Char(string="Medicine")
	dose=fields.Char(string="Dose")
	units=fields.Char(string="Units")
	days=fields.Integer(string="Days")
	Period=fields.Date(string="Period")


