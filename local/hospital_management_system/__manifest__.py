# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'views/in_patient.xml',
        'views/out_patient.xml',
        'views/prescription.xml',
        'views/vaccine.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/bed_management.xml',
        'views/hospital_building.xml',
        'views/ward.xml',
        'views/pharmacy.xml',
        'views/operation_room.xml',
        'views/departments.xml',
        'views/surgeries.xml',
        'views/evaluation.xml',
        'views/labtest.xml',
    ],

}