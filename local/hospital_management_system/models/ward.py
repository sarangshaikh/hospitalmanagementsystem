from odoo import models, fields


class Ward(models.Model):
    _name = 'hospitalmanagement.ward'


    # name = fields.Char(string="Patient Id")
    name=fields.Char(string="Ward Name")

    building_name=fields.Many2one('hospitalmanagement.building',string="Building Name")
    floor_no=fields.Char(string="Floor")
    ward_type=fields.Char(string="Ward Type")
    ac=fields.Boolean(string="AC")
    refrigerator=fields.Boolean(string="Refrigerator")
    tv=fields.Boolean(string="Television")
    internet_access=fields.Boolean(string="Internet Access")
    telephone_access=fields.Boolean(string="Telephone Access")


   