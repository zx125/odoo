# -*- coding: utf-8 -*-
{
    'name': "bug管理系统高级版",

    'summary': """
        管理项目测试过程中发现的bug""",

    'description': """
        管理项目测试过程中发现的bug
    """,

    'author': "zx125",
    'website': "https://www.cnblogs.com/zx125/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bug_manage','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs_stage.xml',
        'views/bugs_adv.xml',
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