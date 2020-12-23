import os
import html

from bottle import Bottle, request, jinja2_view
from bottle import Jinja2Template, url
from bottle import TEMPLATE_PATH

from .config import VIEWS_DIR, config
from .models import db, db_session

app = Bottle(__name__)
app.config.update(config)

# WSGI entry point
application = app

# Update template path
TEMPLATE_PATH[:] = [VIEWS_DIR]

# Location categories
LOCATION_CATEGORIES = {
    7100: "Settlement",
    7200: "Region",
    7300: "Mountain",
    7400: "Glacier",
    7500: "Water",
    7600: "Other",
    7700: "Field"
}

# Decode categories
def get_category(index):
    return LOCATION_CATEGORIES.get(int(index / 100) * 100, "Unknown")

# Update Jinja2 defaults
Jinja2Template.defaults.update({
    'url': url,
    'get_category': get_category,
    'categories': LOCATION_CATEGORIES,
    'title': "DLM Search",
})

def to_number(value):
    try:
        return int(value)
    except ValueError:
        return None

@app.route('/')
@db_session
@jinja2_view('map.html')
def index():
    q = request.query.q.strip()
    category = to_number(request.query.category)
    locations = db.Location.filter_locations(needle=q.lower(), category=category)
    return {'q': q, 'category': category, 'locations': locations}
