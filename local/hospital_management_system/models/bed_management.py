from odoo import models, fields


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
  