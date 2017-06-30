# -*- coding: utf-8 -*-
{
    'name': "First theme",

    'summary': """
        First module created""",

    'description': """
        This is the first theme created by Soluciones4g
    """,

    'author': "OGGonzalezM",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Theme/Creative',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        'views/assets.xml',
        'views/snippets.xml',
    ],
    
    'installable':True,
    'auto_install':False,
}
