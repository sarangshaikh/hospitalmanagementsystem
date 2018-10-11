from odoo import models, fields


class Pharmacy(models.Model):
    _name = 'hospitalmanagement.pharmacy'

    _rec_name='pharmacy_name'

    pharmacy_lines=fields.One2many('hospitalmanagement.pharmacylines','pharmacy_id',string="Pharmacy Lines")

    pharmacy_image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for \
        this contact, limited to 1024x1024px",)
    pharmacy_name =fields.Many2one('res.partner',string="Pharmacy Name")
    build_name=fields.Many2one('hospitalmanagement.building',string="Building Name")
   
    address=fields.Char(related="pharmacy_name.street",string="Address")
    email_id=fields.Char(related="pharmacy_name.email",string="Email")
    phone_no=fields.Char(related="pharmacy_name.phone",string="Phone")
    mobile_no=fields.Char(related="pharmacy_name.mobile",string="Mobile")
    web=fields.Char(related="pharmacy_name.website",string="Website")

    _sql_constraints = ('name_unique','UNIQUE(pharmacy_name)',"Pharmacy Name must be unique"),

    # Prescription_idsss=fields.One2many('hospitalmanagement.prescription','pharmacy_names',string="Prescrription")





class PharmacyLines(models.Model):
    _name='hospitalmanagement.pharmacylines'

    pharmacy_id=fields.Many2one('hospitalmanagement.pharmacy',string="Pharmacy ID")	

    
    # phar_name=fields.Many2many('hospitalmanagement.lines.rel',string="Pharmacy",relation="out_pharmacy_rel")
    patient_id=fields.Char(string="Patient Name") 
    doctor_id=fields.Char(string="Doctor name")
    name=fields.Char(string="Prescription")
    medicines=fields.Char(string="Medicine")
    doses=fields.Float(string="Dose")
    unit=fields.Char(string="Units")
    day=fields.Char(string="Days")
    period=fields.Date(string="Period")


