import os
import csv
import logging

from .models import db, db_session

@db_session
def load(filename):
    if db.Location.select().count():
        return
    logging.info("Importing data...")
    locations = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            category = int(row[0])
            name = row[1].strip()
            var_name = row[2].strip()
            lon = float(row[3])
            lat = float(row[4])
            if not name:
                continue
            locations.append(db.Location(
                category=category,
                name=name,
                var_name=var_name,
                lon=lon,
                lat=lat
            ))
    logging.info("Importing data... done.")
