from odoo import models, fields


class Pharmacy(models.Model):
    _name = 'hospitalmanagement.pharmacy'

    pharmacy_lines=fields.One2many('hospitalmanagement.pharmacylines','pharmacy_id',string="Pharmacy Lines")

    name = fields.Many2one('res.partner',string="Pharmacy Name")
    address=fields.Char(string="Address")
    phone=fields.Integer(string="Phone")
    mobile=fields.Char(string="Mobile")
    email_id=fields.Char(string="Email")
    # web=fields.Char(related="name.website",string="Website")
    # prescription_id=fields.Many2one('hospitalmanagement.prescription',string="Prescription")
    # patient_name=fields.Char(string="Patient Name")


class PharmacyLines(models.Model):
    _name='hospitalmanagement.pharmacylines'

    pharmacy_id=fields.Many2one('hospitalmanagement.pharmacy',string="Pharmacy ID")	

    name=fields.Char(string="Pharmacy")
    pharmacy_name=fields.Many2many('hospitalmanagement.lines.rel',string="Pharmacy",relation="out_pharmacy_rel")
    