# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
from flask_login import LoginManager
from flask_migrate import Migrate
# Allows use of templates and flash methods provided by Bootstrap
from flask_bootstrap import Bootstrap
# from models import ES_PLANT_DIM


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD'

    db.app = app
    db.init_app(app)

    metadata = MetaData()
    tables = ['es_plant_dim']
    metadata.reflect(db.engine, only=tables)
    Base = automap_base(metadata=metadata)

    '''
    class ES_PLANT_DIM(Base):
        __tablename__ = 'es_plant_dim'

        def __repr__(self):
            return '<ES_PLANT_DIM: {}>'.format(self.plant_code)
    '''
    from app import models

    Base.prepare()

    # Base.prepare(db.engine, reflect=True)

    return app
