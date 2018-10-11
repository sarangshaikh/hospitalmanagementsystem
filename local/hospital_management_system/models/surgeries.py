from odoo import models,fields,api,_
from datetime import datetime

class Surgeries(models.Model):
	_name = 'hospitalmanagement.surgeries'

	name = fields.Char(string='Surgeries Id', index=True,
		default=lambda self: _('New'))

	patient_name=fields.Many2one('hospitalmanagement.outpatient',string="Patient name")
	surgery_startdate =fields.Datetime(string="Surgery Date Time")
	surgery_enddate =fields.Datetime(string="Surgery Date Time")
	
	surgeon_name=fields.Many2one('hospitalmanagement.doctor',string="Surgeon")
	assistants=fields.Many2many('hospitalmanagement.doctor',string="Assistants")
	responsible_id=fields.Many2one('res.users',string="Signed By")
	operation_room=fields.Many2one('hospitalmanagement.operationroom',string="Operation Theature")
	mydate=fields.Date(string="Current Date",default=datetime.today())
	states=fields.Selection([
		('draft','Draft'),
		('confirmed','Confirmed'),
		('inprogress','In Progress'),
		('done','Done'),
		('signed','Signed'),
		('cancelled','Cancelled'),
		],string="States")


	state=fields.Selection([
		('signed','Signed'),
		('unsigned','Unsigned'),
		],string="State")
	urgency_level=fields.Selection([
		('urgent','Urgent'),
		('emergency','Emergency'),
		],string="Urgency Level")
	


	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('hospitalmanagement.surgeries') or '/'
			return super(Surgeries, self).create(vals)

	@api.multi
	def action_draft(self):
		self.states ="draft"

	@api.multi
	def action_confirm(self):
		self.states ="confirmed"

	@api.multi
	def action_progress(self):
		self.states = "inprogress"

	@api.multi
	def action_done(self):
		self.states = "done"
		
	@api.multi
	def action_cancel(self):
		self.states = "cancelled"

	@api.multi
	def action_signed(self):
		self.states = "signed"



