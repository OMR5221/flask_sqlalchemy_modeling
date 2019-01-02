# models.py: Represent database tables
# Using sqlalchemy to interact with db
import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
# from app import db, login_manager

db.reflect()

class ES_PLANT_DIM(db.Model):
    __tablename__ = 'es_plant_dim'
    __bind_key__ = 'es_dw_dev'

    # id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<ES_PLANT_DIM: {}>'.format(self.plant_code)

class ES_SCADA_STG1(db.Model):
    __tablename__ = 'es_scada_stg1'
    __bind_key__ = 'es_ods_dev'
    __table_args__ = {'extend_existing': True}
    '''
    __mapper_args__ = {
        'primary_key': [db.Model.] # , 'es_scada_stg1.plant_code', 'es_scada_stg1.timestamplocal']
    }
    '''
    plant_id = db.Column(db.Integer, primary_key=True)
    plant_code = db.Column(db.String(10), primary_key=True)
    tagname = db.Column(db.String(120), primary_key=True)
    timestamplocal = db.Column(db.DateTime, primary_key=True)


    def __repr__(self):
        return '<ES_SCADA_STG1: {}>'.format(self.plant_code)
