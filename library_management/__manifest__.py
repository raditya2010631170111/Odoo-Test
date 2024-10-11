{
    'name': 'Library Management',
    'summary': 'Library Management',
    'description': """
        
    """,
    'author': "Raditya Aji Sasmoyo",

    'website': "https://github.com/raditya2010631170111/Odoo-Test",

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
    'application': True,
    'auto_install': False,
    'external_dependencies': {'python': ['requests','requests_cache'],},
}
