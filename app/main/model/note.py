from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class Note(db.Model):
    """ Note Model for storing note related details """
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    category = db.Column(db.String(255), unique=False, nullable=False)
    is_thesis = db.Column(db.Boolean, nullable=False)
    deal_id = db.Column(db.Integer, db.ForeignKey('deal.id'), nullable=True)
    keywords = db.Column(db.String, nullable=False)

    