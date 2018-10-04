from odoo import models,fields,api,_

class Prescription(models.Model):
	_name = 'hospitalmanagement.prescription'
	prescriptionlines_id=fields.One2many('hospitalmanagement.prescriptionlines','prescription_id',string="PrescriptionLines")



	name = fields.Char(string='Prescription Id', index=True,
		default=lambda self: _('New'))

	patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")

	doctor_id=fields.Many2one('hospitalmanagement.doctor',string="Doctor")

	pharmacy_id=fields.Many2one('hospitalmanagement.pharmacy',string="Pharmacy")

	prescription_date=fields.Date(string="Prescription Date")

	_sql_constraints = ('name_unique','UNIQUE(patient_name)',"Patient Name must be unique"),

	
	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.prescription') or '/'
			return super(Prescription, self).create(vals)

			

class PrescriptionLines(models.Model):
	_name='hospitalmanagement.prescriptionlines'
	
	#relation with prescription(above model)
	prescription_id=fields.Many2one('hospitalmanagement.prescription',string="Prescription Id")
	
	#relation with prescription's name
	prescrip_patient=fields.Many2one(related="prescription_id.patient_name",readonly="1")

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



# @api.onchange('prescrip_patient')
	# def _onchange_prescrip_patient(self):
	# 	if self.prescrip_patient == self.medicine.prescrip_name:
	# 		print("function is working")
	# 		self.medicine=self.medicine.test
	# 	else:
	# 		print("function is not working")





