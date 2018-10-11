from odoo import models, fields,api,_


class OperationRoom(models.Model):
	_name = 'hospitalmanagement.operationroom'

	name = fields.Char(string='Operation Room ID', index=True,
		default=lambda self: _('New'))
	room_name=fields.Char(string="Operation Room")
	building_name= fields.Char(string="Building Name")


	states=fields.Selection([
		('reserved','Mark As Reserved'),
		('occupied','Mark As Occupied'),
		('available','Mark As Available'),
		],string="Status")

	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.operationroom') or '/'
			return super(OperationRoom, self).create(vals)

	@api.multi
	def action_available(self):

		self.states ="available"

	@api.multi
	def action_reserved(self):

		self.states ="reserved"

	@api.multi
	def action_occupied(self):

		self.states ="occupied"




	# @api.multi
	# def action_cancel(self):
	# 	return self.write({'state': 'cancel'})