import os
import html

from bottle import Bottle, request, jinja2_view
from bottle import TEMPLATE_PATH

from .config import VIEWS_DIR, config
from .models import db, db_session

app = Bottle(__name__)
app.config.update(config)

# WSGI entry point
application = app

TEMPLATE_PATH[:] = [VIEWS_DIR]
LIMIT = 1024

def category(category):
    return {
        7100: "Settlement",
        7200: "Region",
        7300: "Mountain",
        7400: "Glacier",
        7500: "Water",
        7600: "Other",
        7700: "Field"
    }.get(int(category / 100) * 100, "Unknown")

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
    return {'q': q, 'category': category, 'locations': locations, 'title': "DLM Search"}
