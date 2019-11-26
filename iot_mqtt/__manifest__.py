# Copyright (C) 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'IoT In',
    'version': '12.0.1.0.0',
    'category': 'IoT',
    'author': "Creu Blanca, "
              "Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'installable': True,
    'summary': 'IoT base module',
    'depends': [
        'iot_output'
    ],
    'external_dependencies': {
        'python': ['paho']
    },
    'data': [
        'data/system_data.xml',
        'views/iot_device_output_views.xml',
    ],
}
