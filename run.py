# run.py: Application entry point
# Starts Flask server and launches the application
import os
from app import create_app, db

# Get the config_name form the user OS Environment Varibale named FLASK_CONFIG:
config_name = os.getenv('FLASK_CONFIG') or 'dev'
app = create_app(config_name)
# app.app_context().push()
#db.create_all(app=app, bind='two')
#db.reflect(app=app, bind='orx_dev_es_dw')

if __name__ == '__main__':
    app.run()
