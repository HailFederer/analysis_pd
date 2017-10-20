import os

# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'service_key': 'oABBCg5E85HSqBojoH367udLslxF44fPv417DVIJvL1MWs1sh7b1xM3RpmQfD6et6jhK%2Fi%2BRADCWmzhFHU2dyg%3D%3D',
        'start_year': 2017,
        'end_year': 2017,
        'restore_directory': '__results__/crawling',
        'fetch': False}}


if not os.path.exists(CONFIG['common']['restore_directory']):
    os.makedirs(CONFIG['common']['restore_directory'])