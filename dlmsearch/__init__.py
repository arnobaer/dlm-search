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

# Limit query results
LOCATIONS_LIMIT = 1024

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

@app.route('/')
@db_session
@jinja2_view('map.html')
def index():
    q = request.query.q.strip()
    category = request.query.category
    category = int(category) if category.isdecimal() else 0
    needle = q.lower()
    if category:
        def filter_locations(location):
            return needle in location.name.lower() and category == location.category
    else:
        def filter_locations(location):
            return needle in location.name.lower()
    def order_locations(location):
        return len(location.name), location.name, len(location.name)
    if q:
        locations = db.Location.select() \
        .filter(filter_locations) \
        .order_by(order_locations) \
        .limit(LOCATIONS_LIMIT)
    else:
        locations = []
    return {'q': q, 'category': category, 'locations': locations}
