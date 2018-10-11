from odoo import models, fields,api,_
from odoo.exceptions import UserError

class Appointment(models.Model):
	_name = 'hospitalmanagement.appointment'


	# name = fields.Char(string="Patient Id")
	name = fields.Char(string='patient Id', index=True,
    default=lambda self: _('New'))
	patient_id= fields.Many2one('res.partner', string="Patient name")

	#relation with evaluation
	# evaluation_id=fields.One2many('hospitalmanagement.evaluation','appointment',string="Evaluation Relation ID")

	appointment_start_date=fields.Datetime(string="Appointment Start DateTime")
	appointment_end_date=fields.Datetime(string="Appointment End DateTime")
	charges=fields.Char(string="Charges")
	doctor_id =fields.Many2one('hospitalmanagement.doctor',string="Doctor")

	# outpatient_rel=fields.One2many("hospitalmanagement.outpatient",'appointment_id',string="Outpatient Relation")
	
	states=fields.Selection([
		('draft','Draft'),
		('requst','Request'),
		('income','Income'),
		],string="Status")


	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.appointment') or '/'
			return super(Appointment, self).create(vals)
	

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
				'doctor':self.doctor_id.name,
				'price_list':self.charges,
				'out_pat_id':orig_ids.id,
			})

			#if you have make relation with another model 
			# and wanna show it's name then you have to add
			#field_name.name.name like below
			# 'doctor':self.doctor_id.name.name,
	









	# @api.multi
	# def compute_appoitment_count(self):
	# 	if states =='income'
			
