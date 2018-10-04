from odoo import models, fields,api,_


class InPatient(models.Model):
    _name = 'hospitalmanagement.inpatient'

    name = fields.Char(string='Inpatient Id', index=True,
    default=lambda self: _('New'))

    # admission_type=fields.Char(string="Admission Type")
    inpatient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")
    doctor_head=fields.Many2one('hospitalmanagement.doctor',string="Doctor Head")
    doctor_in_operation=fields.Many2many('hospitalmanagement.doctor',string="Doctor in Operation")

   
    building_id=fields.Many2one('hospitalmanagement.building',string="Building")
    ward_id=fields.Many2one('hospitalmanagement.ward',string="Ward")
    bed_id=fields.Many2one('hospitalmanagement.bed',string="Bed")
    discharge_date=fields.Datetime(string="Discharge date")

    admission_type=fields.Selection([('urgent','Urgent'),
     ('normal','Normal'),('emergency','Emergency')],string="Admission Type")

    
    _sql_constraints = ('name_unique','UNIQUE(inpatient_name)',"Patient Name must be unique"),
    
      



    @api.model
    def create(self, vals):
      if vals.get('name', _('New')) == _('New'):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.inpatient') or '/'
        return super(InPatient, self).create(vals)





   #  Partner_id=fields.Many2one('res.partner',string="Patient Name")
   #  address=fields.Char(string="Address")
   #  contact_no=fields.Integer(string="Contact No")
    
  	# blood_type=fields.Char(string="Blood Type")
