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
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db' #os.environ.get('DATABASE_1_URI')


    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    # Create a Flask-SQLAlchemy bind for the second database
    SQLALCHEMY_BINDS = {
                        'es_dw_dev': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
                        'es_ods_dev': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD'
    }


    app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

    db.app = app
    db.init_app(app)

    metadata = MetaData()
    es_dw_tables = ['es_plant_dim']
    es_ods_tables = ['es_scada_stg1']
    metadata.reflect(db.get_engine(app, bind='es_dw_dev'), only=es_dw_tables)
    metadata.reflect(db.get_engine(app, bind='es_ods_dev'), only=es_ods_tables)
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
