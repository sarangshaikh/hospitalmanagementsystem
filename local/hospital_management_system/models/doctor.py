from odoo import models, fields


class Doctor(models.Model):
	_name = 'hospitalmanagementsystem.doctor'


	name = fields.Char(string="Doctor Name")

	doc_image = fields.Binary("Image", attachment=True,
		help="This field holds the image used as avatar for \
		this contact, limited to 1024x1024px",)

	degree=fields.Char(string="Degree")
	graduation_institute=fields.Char(string="Graduation Institute")
	consultancy_type=fields.Char(string="Consultancy Type")
	consultancy_charge=fields.Integer(string="Consultancy Charge")
	licence_id= fields.Char(string="Licence_Id")


    