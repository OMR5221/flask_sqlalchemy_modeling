# run.py: Application entry point
# Starts Flask server and launches the application
import os
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
from app import create_app, db
# from app.models import *

# Get the config_name form the user OS Environment Varibale named FLASK_CONFIG:
config_name = os.getenv('FLASK_CONFIG') or 'dev'

app = create_app()

'''
plants = ES_PLANT_DIM.query.all()

for row in plants:
    print(row.plant_code)

st1 = ES_SCADA_STG1.query.first()

print('ES_SCADA_STG1: ' + st1.plant_code)
'''

if __name__ == '__main__':
    app.run()
