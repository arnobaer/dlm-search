import os

PACKAGE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(PACKAGE_DIR, 'data')
VIEWS_DIR = os.path.join(PACKAGE_DIR, 'views')

config = {
    'PONY': {
        'provider': 'sqlite',
        'filename': ':memory:',
        'create_db': True
    }
}
