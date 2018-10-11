from odoo import models, fields,api,_
from odoo.exceptions import UserError


class Vaccine(models.Model):
    _name = 'hospitalmanagement.vaccine'


    name = fields.Char(string='Vaccine', index=True,
        default=lambda self: _('New'))

    @api.model
    def create(self, vals):
      if vals.get('name', _('New')) == _('New'):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.vaccine') or '/'
        return super(Vaccine, self).create(vals)

    vaccine_name =fields.Selection([
    	('hepatitis_a','Hepatitis A'),
    	('hepatitis_b','Hepatitis B'),
    	('influenza','Influenza'),
    	('polio','Polio'),
    	],string="Vaccines",required=True)

    patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient Name")
    dose=fields.Char(string="Dose")
    appointment_date=fields.Date(string="Date")

    # vaccine to outpatient relation    
    out_patient_vac=fields.One2many('hospitalmanagement.outpatient','vaccine_id',string="Vaccine and Out Patient Relation")

    _sql_constraints = ('name_unique','UNIQUE(patient_name)',"patient Name must be unique"),

    @api.multi
    def send_to_outpatient(self):
        vacc_obj= self.env['hospitalmanagement.outpatient']
        print(self.patient_name)
        print(vacc_obj.search([]))
        line_ids = vacc_obj.search([('id', '=', self.patient_name.id)])
        print(line_ids)
        print(self.out_patient_vac.name)

        if  not line_ids:
            raise UserError(_('Patient is not present in Outpatient'))
        else:
            line_ids.out_vaccineline.create({
                'name':self.name,
                'vaccine_name':self.doctor_id.name,
                'patient_name':self.charges,
                'dose':self.dose,
                'appointment_date':self.appointment_date,
                'outpatient_vac_id':line_ids.id,
            })