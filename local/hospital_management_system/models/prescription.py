from odoo import models,fields,api,_
from odoo.exceptions import UserError

class Prescription(models.Model):
	_name = 'hospitalmanagement.prescription'
	prescriptionlines_id=fields.One2many('hospitalmanagement.prescriptionlines','prescriptions_id',string="PrescriptionLines")

	prescription_line=fields.One2many('hospitalmanagement.prescriptionline','prescription_id',string="Prescription Line")

	name = fields.Char(string='Prescription Id', index=True,
		default=lambda self: _('New'))

	patient_names=fields.Many2one('res.partner',string="Patient Name")

	doctor_id=fields.Many2one('hospitalmanagement.doctor',string="Doctor")

	pharmacy_names=fields.Many2one('res.partner',ondelete='cascade',string="Pharmacy")

	prescription_date=fields.Date(string="Prescription Date")

	_sql_constraints = ('name_unique','UNIQUE(patient_names)',"Patient Name must be unique"),

	states=fields.Selection([
		('draft','Draft'),
		('invoice','Invoice'),
		('send','Set To Pharmacy')])


	
	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.prescription') or '/'
			return super(Prescription, self).create(vals)

	@api.multi
	def action_draft(self):

		self.states ="draft"

	#prescription Data transfer to outpatient
	@api.multi
	def action_invoice(self):
		#invoice state
		self.states ="invoice"

		outpatient_obj= self.env['hospitalmanagement.outpatient']
		# print(self.patient_names)
		# print(outpatient_obj.search([]))
		out_ids = outpatient_obj.search([('id', '=', self.patient_names.id)])
		# print(out_ids)
		if  not out_ids:
			raise UserError(_('Patient is not present in Outpatient'))
		else:
			out_ids.out_prescrip_id.create({
				'name':self.name,
				'doctor_name':self.doctor_id.name,	
				'outpatient_id':out_ids.id,
				# 'outpatient_id':self.add_to_offer()
				})
		

			



	@api.multi
	def action_pharmacy(self):

		self.states ="send"

		#prescription Data transfer to pharmacy
		pharmacy_obj= self.env['hospitalmanagement.pharmacy']
		print(self.pharmacy_names)
		print(pharmacy_obj.search([]))
		pharm_ids = pharmacy_obj.search([('id', '=', self.pharmacy_names.id)])
		print(pharm_ids)
		if  not pharm_ids:
			raise UserError(_('Pharmacy_name is not present in Pharmacy'))
		else:
			pharm_ids.pharmacy_lines.create({
				'name':self.name,
				'doctor_id':self.doctor_id.name,	
				'pharmacy_id':pharm_ids.id,
				# 'outpatient_id':self.add_to_offer()
				})


				

class PrescriptionLines(models.Model):
	_name='hospitalmanagement.prescriptionlines'
	
	#relation with prescription(above model)
	prescriptions_id=fields.Many2one('hospitalmanagement.prescription',string="Prescription Id")
	
	#relation with prescription's name
	prescrip_patient=fields.Many2one(related="prescriptions_id.patient_names",readonly="1")

	medicine=fields.Many2one('hospitalmanagement.lines.rel',string="Medicine",domain="[('outpat_prescrip_id','=', prescrip_patient)]")
	
	dose=fields.Float(related="medicine.new_dose",string="Dose",readonly="1")
	units=fields.Char(related="medicine.new_units",string="Units",readonly="1")
	days=fields.Char(related="medicine.new_days",string="Days",readonly="1")
	period=fields.Date(related="medicine.new_period",string="Period",readonly="1")



	@api.onchange('medicine')
	def _onchange_medicine(self):
		if self.medicine:
			self.dose = self.medicine.new_dose
			self.units = self.medicine.new_units
			self.days = self.medicine.new_days
			self.period = self.medicine.new_period




class PrescriptionLine(models.Model):
	_name='hospitalmanagement.prescriptionline'
	
	#relation with prescription(above model)
	prescription_id=fields.Many2one('hospitalmanagement.prescription',string="Prescription Id")
	
	new_medicine=fields.Char(string="Medicine")
	new_dose=fields.Float(string="Dose")
	new_units=fields.Char(string="Units")
	new_days=fields.Char(string="Days")
	new_period=fields.Date(string="Period")

	



	# @api.multi
	# def _get_new_sale_line(self, orig_sale, orig_sale_line):
	# 	res = []
	# 	for line in self.out_prescrip_id:
	# 	res = {
	# 	'order_id': orig_sale_line.order_ids.id,
	# 	'product_id': orig_sale_line.product_ids.id,
	# 	'name': orig_sale_line.product_name,

	# 	}

		# return res

			


	# @api.multi
	# def add_to_offer(self):
	# 	line_env = self.env['hospitalmanagement.outpatient.prescriplines']
	# 	print(self.patient_names)
	# 	print(line_env.search([]))
	# 	out_ids = line_env.search([('name', '=', self.patient_names.id)])
	# 	print(out_ids)
	# 	for rec in self:
			# for rec in wizard.entries:
				# new_line = line_env.create({
				# 	'medicine':rec.new_medicine
				# 	'dose':rec.new_dose
				# 	'units':rec.new_units
				# 	'days':rec.new_days
				# 	'period':rec.new_period
					# 'product_id': what.product_id.id,
					# 'name': what.product_id.name,
					# 'order_id': what.sale_order_id.id,
					# 'product_uom' : what.product_id.uom_id.id
					# })                
        # new_line.product_id_change() #Calling an onchange method to update the record
