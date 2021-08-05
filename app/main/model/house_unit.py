from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class HouseUnit(db.Model):
    """ HouseUnit Model for storing deal related details """
    __tablename__ = "house_unit"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    majorcity = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    area = db.Column(db.String(255), unique=False, nullable=False)
    