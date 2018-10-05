from odoo import models, fields,api,_
from odoo.exceptions import UserError

class Appointment(models.Model):
	_name = 'hospitalmanagement.appointment'


	name = fields.Char(string="Patient Id")
	patient_id= fields.Many2one('res.partner', string="Patient name")



	appointment_datetime =fields.Datetime(string="Appointment DateTime")
	charges=fields.Char(string="Charges")
	doctor_id =fields.Many2one('hospitalmanagement.doctor',string="Doctor")

	# outpatient_rel=fields.One2many("hospitalmanagement.outpatient",'appointment_id',string="Outpatient Relation")
	

	@api.multi
	def send_outpatient(self):
		outpatient_obj= self.env['hospitalmanagement.outpatient']
		print(outpatient_obj.search([]))
		orig_ids = outpatient_obj.search([('name', '=', self.patient_id.id)])
		print(orig_ids)
		if  not orig_ids:
			raise UserError(_('Patient is not present in Outpatient'))
		else:
			orig_ids.out_pat_lines.create({
				'appointment':self.name,
				'doctor':self.doctor_id.name.name,
				'price_list':self.charges,
				'out_pat_id':orig_ids.id,
			})
