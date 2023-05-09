from os import environ


SESSION_CONFIGS = [
    dict(
        name='survey', display_name="调查", app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='dictator',
        display_name="独裁者游戏",
        app_sequence=['dictator', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='prisoner',
        display_name="囚徒游戏",
        app_sequence=['prisoner', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='public_goods_simple',
        display_name="公共物品游戏",
        app_sequence=['public_goods_simple', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='public_goods_punishment',
        display_name="有惩罚的公共物品游戏",
        app_sequence=['public_goods_punishment', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='volunteer_dilemma',
        display_name="志愿者游戏",
        app_sequence=['volunteer_dilemma', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='bargaining',
        display_name="讨价还价游戏",
        app_sequence=['bargaining', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='trust',
        display_name="信任游戏",
        app_sequence=['trust', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='eye',
        display_name="眼睛效应眼睛组",
        app_sequence=['comprehension_test', 'public_goods_eye', 'cooperative_tendency', 'information', 'survey', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='cloud',
        display_name="眼睛效应云朵组",
        app_sequence=['comprehension_test', 'public_goods_cloud', 'cooperative_tendency', 'information', 'survey', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='control',
        display_name="眼睛效应控制组",
        app_sequence=['comprehension_test', 'public_goods_control', 'cooperative_tendency', 'survey', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='0306ex',
        display_name="共情实验组",
        app_sequence=['Trait_empathy', 'sy', 'comprehension_test', 'public_control', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='0306co',
        display_name="共情控制组",
        app_sequence=['Trait_empathy', 'dz', 'comprehension_test', 'public_control', 'payment_info'],
        num_demo_participants=4,
    ),


]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = False

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = True
else:
    DEBUG = False

ROOMS = [
    dict(
        name='econ101',
        display_name='游戏房间1',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='econ102',
        display_name='游戏房间2',
        participant_label_file='_rooms/econ102.txt',
    ),
    dict(
        name='econ103',
        display_name='游戏房间3',
        participant_label_file='_rooms/econ103.txt',
    ),
    dict(
        name='econ104',
        display_name='游戏房间4',
        participant_label_file='_rooms/econ104.txt',
    ),
    dict(name='live_demo', display_name='演示房间'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
有一些小游戏
"""


SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']
