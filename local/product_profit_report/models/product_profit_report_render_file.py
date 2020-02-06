# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class ProductProfitReport(models.Model):
    _name = 'product.profit.report'
    _auto =  False


    name = fields.Many2one('product.product', string="Product")
    id = fields.Integer(string='ID')
    user_id = fields.Many2one('res.users', string="Salesperson")
    external_sale_person = fields.Many2one('res.partner', string="External salesperson")
    invoice_date = fields.Date(string='Invoice Date')
    sale_qty = fields.Float(string="Sale QTY", digits=(16, 2))
    landed_cost = fields.Char(string="Avg Landed Unit Cost", digits=(16, 2))
    avg_pur_price = fields.Char(string="Avg Purchase Unit Price", digits=(16, 2))
    purchase_price = fields.Float(string="Actual Cost", digits=(16, 2),)
    sale_price = fields.Float(string="Sales Amount", digits=(16, 2),)
    net_profit = fields.Float(string="Net Profit", digits=(16, 2),)
    invoice_id = fields.Many2one('account.invoice',string='Invoice')
    profit_percent = fields.Float('Profit %', help='(Sales Amount - Actual Cost)/Sales Amount*100')


    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'product_profit_report')
        self._cr.execute("""
        create or replace view product_profit_report as (
        with avg_pur as ( with landedcost as ( select
        product.id as product_id,
        sum(l.quantity) AS p_qty,        
        sum((l.price_unit - l.discount)) AS price_unit,
        svl.additional_landed_cost AS additional_landed_cost, 
	    svl.quantity as landed_cost_qty
        FROM account_invoice_line l
        left join account_invoice i on (l.invoice_id = i.id) 
        inner join stock_picking sp on (sp.origin = i.origin)
        inner join stock_landed_cost_stock_picking_rel slsp on (slsp.stock_picking_id = sp.id) 
        inner join stock_landed_cost sl on (sl.id = slsp.stock_landed_cost_id)
        inner join stock_valuation_adjustment_lines svl ON (svl.cost_id = sl.id)
        left join product_product product on (product.id=l.product_id)
        left join product_template pt on (pt.id = product.product_tmpl_id)
        where i.type = 'in_invoice' AND i.origin IS NOT NULL AND i.state IN ('open', 'paid') AND i.id NOT IN 
        (SELECT refund_invoice_id FROM account_invoice WHERE state IN ('paid','open') AND refund_invoice_id IS NOT NULL
         UNION
         SELECT id FROM account_invoice WHERE state IN ('paid','open') AND refund_invoice_id IS NOT NULL)
        AND product.id IS NOT NULL AND product.id = svl.product_id
        group by product.id, svl.additional_landed_cost,svl.quantity
        having sum(l.quantity) != 0) 
        SELECT product_id,
       ROUND((sum(additional_landed_cost)/sum(landed_cost_qty)),2) as landed_cost, p_qty, price_unit from landedcost 
       group by p_qty, price_unit, product_id
       ) SELECT row_number() over(order by ap.product_id) as id, landed_cost,
       ap.product_id as name, i.id as invoice_id,
       i.user_id,
        i.external_sale_person,
        i.date_invoice AS invoice_date,
        sum(l.quantity) AS sale_qty,        
        sum(l.quantity * (l.price_unit - l.discount)) AS sale_price,
        ROUND(sum((ap.price_unit+landed_cost)*p_qty)/sum(p_qty),2) as avg_pur_price,
        (sum(l.quantity)* (sum((ap.price_unit+landed_cost)*p_qty)/sum(p_qty))) AS purchase_price,
        sum(l.quantity * (l.price_unit - l.discount)) - (sum(l.quantity)* (sum((ap.price_unit+landed_cost)*p_qty)/sum(p_qty))) as net_profit,
        (sum(l.quantity * (l.price_unit - l.discount)) - (sum(l.quantity)* (sum((ap.price_unit+landed_cost)*p_qty)/sum(p_qty))))/NULLIF(sum(l.quantity * (l.price_unit - l.discount)), 0)*100 as profit_percent
        FROM account_invoice_line l
        left join account_invoice i on (l.invoice_id = i.id)
        inner join res_users u on (u.id = i.user_id)
        left join product_product product on (product.id=l.product_id)
        left join product_template pt on (pt.id = product.product_tmpl_id)
        inner join avg_pur ap on (ap.product_id=product.id) where i.type = 'out_invoice' AND i.state IN ('open', 'paid') AND i.id NOT IN 
        (SELECT id FROM account_invoice WHERE state IN ('paid','open') AND refund_invoice_id IS NOT NULL)
        AND product.id IS NOT NULL group by ap.product_id, i.external_sale_person, i.user_id, i.id, landed_cost, ap.product_id       
        having sum(l.quantity) != 0
       )""")

