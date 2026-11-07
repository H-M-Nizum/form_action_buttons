{
    'name': 'Form Save & Discard Buttons',
    'summary': 'Replace the tiny save/discard icons of every form with two real, colourful buttons',
    'description': 'Shows "Save" and "Discard" buttons in the top-left corner of every form view, '
                   'with configurable background and text colours.',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'author': 'H.M.Nizum',
    'maintainer': 'H.M.Nizum',
    'website': 'https://github.com/H-M-Nizum/form_action_buttons',
    'license': 'LGPL-3',
    'depends': ['web', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'form_action_buttons/static/src/form_status_indicator.js',
            'form_action_buttons/static/src/form_status_indicator.xml',
            'form_action_buttons/static/src/form_status_indicator.scss',
        ],
        'web.assets_tests': [
            'form_action_buttons/static/src/tour.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/screenshots/01_default.png',
        'static/description/screenshots/02_custom_colors.png',
        'static/description/screenshots/03_settings.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
