from odoo import models, fields,api


class OutPatient(models.Model):
    _name = 'hospitalmanagement.outpatient'

    out_pat_lines=fields.One2many('hospitalmanagement.outpatientlines',
        'out_pat_id',string="Out Patient Lines")
     # out_pat_lines=fields.One2many('res.partner',related="name.child_id",string="Out Patient Lines")

    prescription_line_rel=fields.One2many('hospitalmanagement.lines.rel','outpat_prescrip_id',string="prescription rel")


    image = fields.Binary("Image", attachment=True,
      help="This field holds the image used as avatar for \
      this contact, limited to 1024x1024px",)

    name=fields.Many2one('res.partner',string="Patient Name")    

    birth_date=fields.Date(string="Date Of Birth")
    
    blood_type=fields.Selection([('a','A'),
     ('b','B'),('o','O')],string="Admission Type")
    
    rh_id=fields.Selection([('-','-'),
     ('+','+'),('notdefined','Not Defined')],string="RH")
    
    gender=fields.Selection([('male','Male'),
     ('female','Female')],string="Gender")
    
    responsible_id=fields.Many2one('res.users',string="Responsible")
    
    marital_id=fields.Selection([('single','Single'),
     ('married','Married'),('divorced','Divorced')],string="marital Status")

    
    doctor_name=fields.Many2one('hospitalmanagement.doctor',string="Doctor Name")

    description_id=fields.Text(string="Description")   

    #Sql constraint for unique name of patient 
    _sql_constraints = ('name_unique','UNIQUE(name)',"Out patient must be unique"),




class OutPatientLines(models.Model):

    _name = 'hospitalmanagement.outpatientlines'

    out_pat_id= fields.Many2one('hospitalmanagement.outpatient',
        string="Out Patient Id")


    contact_no=fields.Integer(string="Contact No")
    address=fields.Char(string="Address")






class Prescription_lines_rel(models.Model):
    _name='hospitalmanagement.lines.rel'

    #Relation  with outpatient 
    outpat_prescrip_id=fields.Many2one('hospitalmanagement.outpatient',string="Prescription in outpatient")

    name=fields.Char(string="Name",store=True)
    new_dose=fields.Float(string="Dose",store = True)
    new_units=fields.Char(string="Units",store=True)
    new_days=fields.Char(string="Days",store=True)
    new_period=fields.Date(string="Period",store=True)


    #relation with name of Out patient
    prescrip_name=fields.Many2one(related="outpat_prescrip_id.name", string="Prescription Patient")










