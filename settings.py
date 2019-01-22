from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'SHOCKS_1',
        'display_name': "SHOCKS_1",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Memory', 'Raven', 'Dados', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'SHOCKS_2',
        'display_name': "SHOCKS_2",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Memory', 'Dados', 'Raven', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'SHOCKS_3',
        'display_name': "SHOCKS_3",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Raven', 'Memory', 'Dados', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'SHOCKS_4',
        'display_name': "SHOCKS_4",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Raven', 'Dados', 'Memory', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'SHOCKS_5',
        'display_name': "SHOCKS_5",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Dados', 'Memory', 'Raven', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'SHOCKS_6',
        'display_name': "SHOCKS_6",
        'num_demo_participants': 4,
        'app_sequence': ['Consent', 'Sumas', 'Dados', 'Raven', 'Memory', 'Lottery', 'Question', 'Report'],
        'use_browser_bots': False
    },
    {
        'name': 'Single_App_Try',
        'display_name': "SAT",
        'num_demo_participants': 4,
        'app_sequence': ['Sumas', 'Question', 'Report'],
        'use_browser_bots': False
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0
POINTS_CUSTOM_NAME = ''
USE_POINTS = True

ROOMS = [
    {
        'name': 'Estudio',
        'display_name': 'Estudio',
    }
]

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'FelipeM'
# for security, best to set admin password in an environment variable
#ADMIN_PASSWORD = 'felmola0323'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'k7@k%23a5o1a6*4%04b1!uj0!h(+s9y(!lj3fcjhsn8zrt8#ux'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

SENTRY_DSN = environ.get('SENTRY_DSN')
