{
    'name': 'Library Management',
    'summary': 'Library Management',
    'description': """
        Submenu baru pada menu Accounting yang memiliki fitur untuk meminta atau mengembalikan uang kepada finance
    """,
    'author': "PT. Ismata Nusantara Abadi",

    'website': "https://ismata.co.id/",

    'category': 'Tools',

    
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'data/demo_data.xml',
    ],
    # 'images': [],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
