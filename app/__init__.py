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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD'
metadata = MetaData()
tables = ['es_plant_dim']
db = SQLAlchemy(app, metadata=metadata)
metadata.reflect(db.engine, only=tables)
Base = automap_base(metadata=metadata)

"""
class ES_PLANT_DIM(Base):
    __tablename__ = 'es_plant_dim'

    def __repr__(self):
        return '<ES_PLANT_DIM: {}>'.format(self.plant_code)
"""
from models import *

Base.prepare()
# Base.prepare(db.engine, reflect=True)

#data = db.session.query(ES_PLANT_DIM).all()

#for row in data:
#    print(row.plant_code)

if __name__ == "__main__":
    # show the table schema
    # print(Table1.__table__.c)

    data = db.session.query(ES_PLANT_DIM).all()

    for row in data:
        print(row.plant_code)
