import os
import html

from bottle import Bottle, request, jinja2_view
from bottle import TEMPLATE_PATH

from .config import VIEWS_DIR, DATA_DIR, config
from .models import db, db_session
from .loader import load

app = Bottle(__name__)
app.config.update(config)

TEMPLATE_PATH[:] = [VIEWS_DIR]
LIMIT = 1024

load(os.path.join(DATA_DIR, 'default.csv'))

@app.route('/')
@db_session
@jinja2_view('map.html')
def index():
    q = request.query.get('q', '')
    needle = q.lower().strip()
    locations = []
    if q:
        locations = db.Location\
            .select()\
            .filter(lambda l: needle in l.name.lower())\
            .order_by(lambda l: (len(l.name), l.name, len(l.name)))\
            .limit(LIMIT)
    return {'q': q, 'locations': locations, 'title': "DLM Search"}
