# -*- coding: utf-8 -*-

{
    'name': 'Product Profit Report',
    'version': '11.0.',
    'summary': 'Product wise profit report',
    'category': 'Urbia',
    'author': "Comstar USA Inc.",
    'website': "http://www.comstarusa.com",
    'depends': ['base','sale_management', 'account_invoicing'
    ],
    'data': [
        'wizard/product_profit_report_wizard_view.xml',
        'views/product_profit_report_report.xml',

    ],
    'license': 'AGPL-3',

}
