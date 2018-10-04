from odoo import models,fields,api,_


class HospitalBuilding(models.Model):
    _name = 'hospitalmanagement.building'

    name=fields.Char(string="Building Code")
    building_name=fields.Char(string="Building Name")
  	
    @api.model
    def create(self, vals):
    	if vals.get('name', _('New')) == _('New'):
    		vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.building') or '/'
    		return super(HospitalBuilding, self).create(vals)
