from odoo import models, fields


class InPatient(models.Model):
    _name = 'hospitalmanagementsystem.inpatient'

    name = fields.Char(string="Patient Id")
    admission_type_id=fields.Char(string="Admission Type")

    # doctor_in_operation=fields.Many2many('res.user',string="Doctor in Operation")
    doctor_head=fields.Many2one('res.user',string="Doctor Head")
    building_id=fields.Char(string="Building")
    ward_id=fields.Char(string="Ward")
    bed_id=fields.Char(string="Bed")
    discharge_date=fields.Datetime(string="Discharge date")



   #  Partner_id=fields.Many2one('res.partner',string="Patient Name")
   #  address=fields.Char(string="Address")
   #  contact_no=fields.Integer(string="Contact No")
    
  	# blood_type=fields.Char(string="Blood Type")