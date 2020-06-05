# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        图书管理系统""",

    'description': """
        图书管理系统
    """,

    'author': "zx125",
    'website': "http://www.cnblog.zx125.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/views.xml',
        'views/book_view.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 模型转app
    'application': True,
    # 排序第一位
    'sequence': 1,
}
