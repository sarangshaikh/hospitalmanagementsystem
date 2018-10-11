from odoo import models, fields,api,_


class LabTest(models.Model):
	_name = 'hospitalmanagement.labtest'

	name = fields.Char(string='Lab Test #', index=True,
		default=lambda self: _('New'))

	# doctor_name=fields.Many2one('hospitalmanagement.doctor',string="Doctor Name")
	# patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")
	# evaluation_start_date=fields.Datetime(string="Evaluation Start Date")
	# evaluation_end_date=fields.Datetime(string="Evaluation End Date")
	# evaluation_type=fields.Selection([
	# 	('urgent','Urgent'),
	# 	('ambulatory','Ambulatory'),
	# 	('emergency','Emergency'),
	# 	],string="Evaluation Type")
	# appointment=fields.Many2one('hospitalmanagement.appointment',string="Appointment ID")
	# appointment_date=fields.Date(string="Appointment Date")


	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.labtest') or '/'
			return super(LabTest, self).create(vals)
