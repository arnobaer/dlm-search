import os

PACKAGE_DIR = os.path.dirname(__file__)
VIEWS_DIR = os.path.join(PACKAGE_DIR, 'views')

config = {
    'PONY': {
        'provider': 'sqlite',
        'filename': 'local.db',
        'create_db': True
    }
}
