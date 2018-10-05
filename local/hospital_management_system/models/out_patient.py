from odoo import models, fields,api,_


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

    appointment_id=fields.Many2one('hospitalmanagement.appointment',string="Appointment ID")


    
    @api.depends("appointment_id")
    def _compute_appointments(self):
        for rec in self:
            print(self.appointment_id)
            rec.appointment_count=len(rec.appointment_id)
    
    appointment_count=fields.Integer(string="Appointments",compute="_compute_appointments")


    @api.multi
    def action_view_appointment(self):
        return {
            'name': _('Patient appointment'),
            'view_mode': 'form',
            'view_id': self.env.ref('hospital_management.outpatient_form_view').id,
            'res_model': 'hospitalmanagement.appointment',
            # 'context': "{'type':'out_invoice'}",
            'type': 'ir.actions.act_window',
            'res_id': self.appointment_id.id,
        }




class OutPatientLines(models.Model):

    _name = 'hospitalmanagement.outpatientlines'

    out_pat_id= fields.Many2one('hospitalmanagement.outpatient',
        string="Out Patient Id")

    patient_name=fields.Many2one(related="out_pat_id.name", string="outlinesPatient")

    contact_no=fields.Integer(string="Contact No")
    address=fields.Char(string="Address")
    appointment=fields.Char(string="Appointment Id")
    doctor=fields.Char(string="Doctor")
    price_list=fields.Char(string="Price List")



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










