from odoo import models, fields


class Doctor(models.Model):
    _name = 'hospitalmanagementsystem.doctor'


    name = fields.Char(string="Patient Id")
    partner_id= fields.Many2one('res.partner', string="Patient name")