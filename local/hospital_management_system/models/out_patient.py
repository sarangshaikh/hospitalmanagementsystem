from odoo import models, fields


class OutPatient(models.Model):
    _name = 'hospitalmanagementsystem.outpatient'

    out_pat_lines=fields.One2many('hospitalmanagementsystem.outpatientlines',
        'out_pat_id',string="Out Patient Lines")

    image = fields.Binary("Image", attachment=True,
      help="This field holds the image used as avatar for \
      this contact, limited to 1024x1024px",)
    name=fields.Many2one('res.partner',string="Patient Name")    

    birth_date=fields.Date(string="Date Of Birth")
    blood_type=fields.Char(string="Blood Type")
    gender=fields.Char()
    responsible_id=fields.Char(string="Responsible")
    maritial_id=fields.Char(string="Martial Status")
    rh_id=fields.Char(string="Rh")
    doctor_name=fields.Many2one('res.user',string="Doctor Name")


    description_id=fields.Char(string="Description")
    
    





class OutPatientLines(models.Model):

    _name = 'hospitalmanagementsystem.outpatientlines'

    out_pat_id= fields.Many2one('hospitalmanagementsystem.outpatient',
        string="Out Patient Id")

    name = fields.Char(string="Patient Id")
    contact_no=fields.Integer(string="Contact No")
    address=fields.Char(string="Address")