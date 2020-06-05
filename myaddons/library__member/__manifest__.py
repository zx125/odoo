# -*- coding: utf-8 -*-
{
    'name': "Library Member",

    'summary': """
        图书馆借书功能""",

    'description': """
        图书馆借书功能
    """,

    'author': "zx125",
    'website': "https://www.cnblogs.com/zx125/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_list_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 模型转app
    'application': False,
    # 排序第一位
    'sequence': 1,
}