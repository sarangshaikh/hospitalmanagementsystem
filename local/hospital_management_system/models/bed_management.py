from odoo import models, fields,api


class Bed(models.Model):
	_name = 'hospitalmanagement.bed'


	name = fields.Char(string="Bed Code")
	building_id=fields.Char(string="Building")
	ward=fields.Char(string="Ward")
	charges=fields.Char(string="Reservation Charges")
	bed_type=fields.Selection([
		('electrical','Electrical'),
		('manual','Manual'),
		('auto','Auto'),
		],string="Bed Type")

	status=fields.Selection([
		('free','Free'),
		('reserved','Reserved'),
		('occupied','Occupied'),
		('notavailable','Not Available'),
		],string="Bed Status")
  


	@api.multi
	def action_free(self):
		self.status ="free"

	@api.multi
	def action_reserved(self):
		self.status ="reserved"

	@api.multi
	def action_occupied(self):
		self.status ="occupied"

	@api.multi
	def action_notavailable(self):
		self.status ="notavailable"


