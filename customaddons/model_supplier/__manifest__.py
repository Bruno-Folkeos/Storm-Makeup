# -*- coding: utf-8 -*-
{
    'name': "Módulo Fornecedor",

    'summary': """
       Módulo de Fornecedores""",

    'description': """
        Módulo que insere campo fornecedor no cadastro de contato.
    """,

    'author': "Bruno",

    'category': 'supplier',
    'version': '0.1',

    'depends': [
        'base'
        ],

    'data': [
        'views/res_partner_views.xml'
    ],

    "installable": True,
    "application": True,
}