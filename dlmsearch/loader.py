import os
import csv

from .models import db, db_session

@db_session
def import_csv(filename):
    print("Importing data...")
    locations = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            category = int(int(int(row[0]) / 100) * 100) # reduce
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
    print("Importing data... done.")
