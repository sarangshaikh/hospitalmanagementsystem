from odoo import models, fields


class Doctor(models.Model):
	_name = 'hospitalmanagement.doctor'


	name = fields.Many2one('res.users',string="Doctor Name")

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


	consultancy_type=fields.Char(string="Consultancy Type")
	consultancy_charge=fields.Integer(string="Consultancy Charge")
	licence_id= fields.Char(string="Licence_Id")

	department=fields.Many2one('hospitalmanagement.departments',string="Departments")
	# department_names=fields.Many2one(related="department.department_name",string="Department")
	_sql_constraints = ('name_unique','UNIQUE(name)',"Doctor's Name must be unique"),
	

