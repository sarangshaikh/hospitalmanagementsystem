from odoo import models, fields,api,_



class Departments(models.Model):
    _name = 'hospitalmanagement.departments'

    #department_id=fields.Char(string="Department")


    name = fields.Char(string='Department Id', index=True,
    default=lambda self: _('New'))


    department_name=fields.Char(string="Department Name")
    building_name=fields.Many2one('hospitalmanagement.building',string="Building Name")
    floor_id=fields.Selection([
    	('1stfloor','1st Floor'),
    	('2ndfloor','2nd Floor'),
    	('3rdfloor','3rd Floor'),
    	('4thfloor','4th Floor'),
    	('5rdfloor','5th Floor'),
    	],string="Floor")


    @api.model
    def create(self, vals):
      if vals.get('name', _('New')) == _('New'):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.departments') or '/'
        return super(Departments, self).create(vals)
