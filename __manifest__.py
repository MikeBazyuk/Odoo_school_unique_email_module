{
    'name': 'Partner Unique Email',
    'summary': 'Забороняє наявність у системі декількох партнерів з однаковим e-mail',
    'description': """
Partner Unique Email
====================

Розширення базової моделі **res.partner**, яке гарантує унікальність
e-mail адреси серед усіх партнерів у системі.

Функціонал
----------
* Перевірка виконується при створенні та редагуванні партнера.
* Порівняння e-mail є регістронезалежним (case-insensitive).
* Порожнє поле e-mail не обмежується — кілька партнерів можуть
  не мати e-mail взагалі.
* Виводиться зрозуміле повідомлення з дублюючою адресою.
    """,
    'author': 'Mykhailo Baziuk',
    'website': 'https://odoo.school/',
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'version': '19.0.1.0.0',

    'depends': ['base'],

    'external_dependencies': {
        'python': [],
    },

    'data': [],

    'demo': [],

    'images': [
        'static/description/banner.png',
    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
