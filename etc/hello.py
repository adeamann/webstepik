#!/usr/bin/python3
CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    'python': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        'ask.wsgi:application',
    ),
}
