from odoo import models, fields


class Vaccine(models.Model):
    _name = 'hospitalmanagement.vaccine'


    name = fields.Char(string="Vaccine Id")
    vaccine_name=fields.Selection([
    	('hepatitis_a','Hepatitis A'),
    	('hepatitis_b','Hepatitis B'),
    	('influenza','Influenza'),
    	('polio','Polio'),
    	],string="Vaccines")
    patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")
    dose=fields.Char(string="Dose")
    appointment_date=fields.Date(string="Date")
