# run.py: Application entry point
# Starts Flask server and launches the application
import os
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
from app import create_app, db

# Get the config_name form the user OS Environment Varibale named FLASK_CONFIG:
config_name = os.getenv('FLASK_CONFIG') or 'dev'

app = create_app()

"""
data = db.session.query('es_plant_dim').all()

for row in data:
    print(row.plant_code)
"""

if __name__ == '__main__':
    app.run()
