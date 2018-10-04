from odoo import models, fields


class OperationRoom(models.Model):
    _name = 'hospitalmanagement.operationroom'


    name = fields.Char(string="Operation Room Id")
    room_name=fields.Char(string="Operation Room")
    building_name= fields.Char(string="Building Name")


  