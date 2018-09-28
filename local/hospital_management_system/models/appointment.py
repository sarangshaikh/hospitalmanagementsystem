from odoo import models, fields


class Appointment(models.Model):
    _name = 'hospitalmanagementsystem.appointment'


    name = fields.Char(string="Patient Id")
    patient_app = fields.Many2one('res.partner', string="Patient name")