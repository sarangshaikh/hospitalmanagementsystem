from odoo import models, fields,api,_


class Evaluation(models.Model):
	_name = 'hospitalmanagement.evaluation'

	name = fields.Char(string='Evaluation #', index=True,
		default=lambda self: _('New'))

	doctor_name=fields.Many2one('hospitalmanagement.doctor',string="Doctor Name")
	patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")
	evaluation_start_date=fields.Datetime(string="Evaluation Start Date")
	evaluation_end_date=fields.Datetime(string="Evaluation End Date")
	evaluation_type=fields.Selection([
		('urgent','Urgent'),
		('ambulatory','Ambulatory'),
		('emergency','Emergency'),
		],string="Evaluation Type")

	appointment=fields.Many2one('hospitalmanagement.appointment',string="Appointment ID")
	appointment_date=fields.Date(string="Appointment Date")


	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.evaluation') or '/'
			return super(Evaluation, self).create(vals)


	#prescription Data transfer to outpatient
	@api.multi
	def action_data_transfer(self):
	
		

		outpat_obj= self.env['hospitalmanagement.outpatient']
		# print(self.patient_names)
		# print(outpatient_obj.search([]))
		out_ids = outpat_obj.search([('id', '=', self.patient_name.id)])
		# print(out_ids)
		if  not out_ids:
			raise UserError(_('Patient is not present in Outpatient'))
		else:
			out_ids.out_evaluationline.create({
				'name':self.name,
				'doctor_name':self.doctor_name.name,
				'evaluation_start_date':self.evaluation_start_date,
				'evaluation_end_date':self.evaluation_end_date,
				'patient_name':self.patient_name,
				'evaluation_type':self.evaluation_type,
				'outpatient_eval_id':out_ids.id,
				'appointment':self.appointment,
				# 'outpatient_id':self.add_to_offer()
				})