from odoo import models, fields


class Vaccine(models.Model):
    _name = 'hospitalmanagementsystem.vaccine'


    name = fields.Char(string="Vaccine Id")
    vaccine_name=fields.Char(string="Vaccines")
    patient_name=fields.Many2one('hospitalmanagementsystem.outpatient',string="Patient Name")
    dose=fields.Char(string="Dose")
    appointment_date=fields.Date(string="Date")
