# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api,_


class ProductProfitwizard(models.TransientModel):
    _name = "product.profit.wizard"
    _description = 'Product Profit Wizard'



    def _get_from_date(self):
        company = self.env.user.company_id
        current_date = datetime.date.today()
        from_date = company.compute_fiscalyear_dates(current_date)['date_from']
        return from_date

    from_date = fields.Date(string='From Date', default=_get_from_date, required=True)
    to_date = fields.Date(string='To Date', default=fields.Date.context_today, required=True)
    company = fields.Many2one('res.company', string='Company', required=True,
                              default=lambda self: self.env.user.company_id.id)
    user_id = fields.Many2many('res.users',string="Multiple Salesperson", store="True", domain= lambda self:[('external_users','=','False')])

    external_sale_person = fields.Many2many('res.partner', string='External Salesperson',store="True",
                                           domain="[('related_user','=', user_id)]")
    is_salesperson_external = fields.Boolean(string="Is Salesperson External")
    is_external = fields.Boolean(string="Is External Salesperson",help="Check to select Urbia Outside sales in salesperson and uncheck to select multiple  Internal Salesperson")

    # report_rel = fields.Many2one('product.profit.report',string="report rel")


    @api.onchange('is_external')
    def _onchange_is_external(self):
        if self.is_external:
            self.write({'user_id': False})
            return {
                'domain': {'user_id': [('external_users', '=', True)]}
            }
        elif self.is_external ==False:
            self.write({'user_id': False})
            return {
                'domain': {'user_id': [('external_users', '=', False)]}
            }


    @api.onchange('user_id','external_sale_person')
    def _onchange_user_id_products(self):

        for rec in self:
            if rec.user_id:
                for users in rec.user_id:
                    if users.external_users == True:
                        rec.is_salesperson_external = True

                    elif users.external_users == False:
                        rec.external_sale_person = False
                        rec.is_salesperson_external = False

            else:
                rec.external_sale_person = False
                rec.is_salesperson_external = False
 

    @api.multi
    def action_open_window(self):
        self.ensure_one()

        context = dict(self.env.context or {})

        def ref(module, xml_id):
            proxy = self.env['ir.model.data']
            return proxy.get_object_reference(module, xml_id)

        model, pivot_view_id = ref('product_profit_report', 'view_product_profit_report_report_pivot')
        model, tree_view_id = ref('product_profit_report', 'view_product_profit_report_tree')

        users = []
        external_users = []
        for rec in self:
            # rec.report_rel.generate_report_val()
            context.update(is_salesperson_external=rec.is_salesperson_external)
            if rec.user_id:
                if rec.is_salesperson_external == False:
                    # users = rec.user_id.ids
                    domain = [
                        ('user_id', 'in', rec.user_id.ids),
                        ('invoice_date', '>=', rec.from_date),
                        ('invoice_date', '<=', rec.to_date),
                    ]
                elif rec.is_salesperson_external == True:
                    domain = [
                        ('external_sale_person', 'in', rec.external_sale_person.ids),
                        ('invoice_date', '>=', rec.from_date),
                        ('invoice_date', '<=', rec.to_date),

                    ]
            else:
                domain = [
                    ('invoice_date', '>=', rec.from_date),
                    ('invoice_date', '<=', rec.to_date),
                ]



        views = [
            (tree_view_id, 'tree'),
            (pivot_view_id, 'pivot')
        ]



        return {
            'name': _('Product Profit Report'),
            'context': context,
            'view_type': 'form',
            "view_mode": 'pivot,tree',
            'res_model': 'product.profit.report',
            'type': 'ir.actions.act_window',
            'views': views,
            'view_id': False,
            # 'search_view_id':search_view_id,
            'domain': domain
        }


