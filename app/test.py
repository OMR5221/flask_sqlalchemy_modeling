# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.automap import automap_base
from flask_login import LoginManager
from flask_migrate import Migrate
# Allows use of templates and flash methods provided by Bootstrap
from flask_bootstrap import Bootstrap


app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db' #os.environ.get('DATABASE_1_URI')


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Create a Flask-SQLAlchemy bind for the second database
SQLALCHEMY_BINDS = {
                    'es_dw_dev': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
                    'es_ods_dev': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD'
}


app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

# Need to give SQLAlchemy object the current app context
with app.app_context():
    # Create an engine for the db2 bind
    engine = db.get_engine(app, bind='es_dw_dev')

    # Create a new session using the db2-bound
    # engine.  This is a Flask-SQLAlchemy
    # SignallingSession and should behave
    # the same way as db.session (have not
    # tested
    # yet but
    # docs
    # say it
    # will)
    Session = db.create_scoped_session({'bind': engine})
    db2_session = Session()

meta = MetaData(engine)
plant_dim_table = Table('es_plant_dim', meta, autoload=True, autoload_with=engine)

data = db2_session.query(plant_dim_table).all()

for row in data:
    print(row.plant_code)
