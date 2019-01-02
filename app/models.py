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

    def __repr__(self):
        return '<ES_PLANT_DIM: {}>'.format(self.plant_code)
