from odoo import models, fields,api,_


class Doctor(models.Model):
	_name = 'hospitalmanagement.doctor'


	name = fields.Char(string="Doctor Name")

	doc_image = fields.Binary("Image", attachment=True,
		help="This field holds the image used as avatar for \
		this contact, limited to 1024x1024px",)

	graduation_institute=fields.Selection([
		('neurology','Neurology'),
		('immunology','Immunology'),
		('cardiology','Cardiology'),
		('physiotherapy','Physiotherapy'),
		('gynecology','Gynecology'),
		('psycology','Psycology')
		],string="Degree")

	degree=fields.Selection([
		('neurologist','Neurologist'),
		('immunologist','Immunologist'),
		('cardiologist','Cardiologist'),
		('familyphysian','Family Physian'),
		('gynecologist','Gynecologist'),
		('pediatric','Pediatric'),
		('pychiatrists','Pychiatrists')
		],string="Degree")


	consultancy_type=fields.Selection([
		('private','Private'),
		('public','Public'),
		],string="Consultancy Type")
	consultancy_charge=fields.Integer(string="Consultancy Charge")
	licence_id= fields.Char(string="Licence_Id")

	department=fields.Many2one('hospitalmanagement.departments',string="Departments")
	# department_names=fields.Many2one(related="department.department_name",string="Department")
	_sql_constraints = ('name_unique','UNIQUE(name)',"Doctor's Name must be unique"),
	

	appoint_id=fields.Many2one('hospitalmanagement.appointment',string="Appointment ID")
	appoint_count=fields.Integer(string="Appointments",compute="_compute_appoints")



	@api.depends("appoint_id")
	def _compute_appoints(self):
		for rec in self:
			print(self.appoint_id)
			rec.appoint_count=len(rec.appoint_id)


	@api.multi
	def action_view_appointment(self):
		return {
		'name': _('Patient appointment'),
		'view_mode': 'tree',
		'view_id': self.env.ref('appointment_tree_view').id,
		'res_model': 'hospitalmanagement.appointment',
		# 'context': "{'type':'out_invoice'}",
		'type': 'ir.actions.act_window',
		'res_id': self.id,
		}


