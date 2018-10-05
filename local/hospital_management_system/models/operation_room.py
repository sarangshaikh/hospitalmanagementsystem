from odoo import models, fields,api,_


class OperationRoom(models.Model):
	_name = 'hospitalmanagement.operationroom'

	name = fields.Char(string='Operation Room ID', index=True,
		default=lambda self: _('New'))
	room_name=fields.Char(string="Operation Room")
	building_name= fields.Char(string="Building Name")


	state=fields.Selection([
		('reserved','Mark As Reserved'),
		('occupied','Mark As Occupied'),
		('available','Mark As Available'),
		],string="Status")

	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.operationroom') or '/'
			return super(OperationRoom, self).create(vals)