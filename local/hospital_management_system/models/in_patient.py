from odoo import models, fields,api,_


class InPatient(models.Model):
    _name = 'hospitalmanagementsystem.inpatient'

    name = fields.Char(string='Prescription Id', index=True,
    default=lambda self: _('New'))

    admission_type_id=fields.Char(string="Admission Type")
    inpatient_name=fields.Many2one('hospitalmanagementsystem.outpatient',string="Patient Name")
    # doctor_in_operation=fields.Many2many('hospitalmanagementsystem.doctor',string="Doctor in Operation")

    doctor_head=fields.Many2one('hospitalmanagementsystem.doctor',string="Doctor Head")
    building_id=fields.Char(string="Building")
    ward_id=fields.Char(string="Ward")
    bed_id=fields.Char(string="Bed")
    discharge_date=fields.Datetime(string="Discharge date")



    @api.model
    def create(self, vals):
      if vals.get('name', _('New')) == _('New'):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagementsystem.inpatient') or '/'
        return super(InPatient, self).create(vals)


   #  Partner_id=fields.Many2one('res.partner',string="Patient Name")
   #  address=fields.Char(string="Address")
   #  contact_no=fields.Integer(string="Contact No")
    
  	# blood_type=fields.Char(string="Blood Type")
