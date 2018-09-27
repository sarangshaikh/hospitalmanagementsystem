from odoo import models, fields


class Vaccine(models.Model):
    _name = 'hospitalmanagementsystem.vaccine'


    name = fields.Char(string="Patient Id")
    partner_id= fields.Many2one('res.partner', string="Patient name")