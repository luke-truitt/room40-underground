from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class Housemodel(db.Model):
    """ Deal Model for storing deal related details """
    __tablename__ = "houseunit"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    houseunit_id=db.Column(db.Integer, db.ForeignKey('houseunit.id'))
    project_oneyear = db.Column(db.Integer, unique=False, nullable=False)
    project_twoyear = db.Column(db.Integer, unique=False, nullable=False)
    project_fiveyear = db.Column(db.Integer, unique=False, nullable=False)