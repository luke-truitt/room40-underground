from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class DealInvestor(db.Model):
    """ DealInvestor Model is used to link deals to their respective investors """
    __tablename__ = "deal_investor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deal_id = db.Column(db.Integer, db.ForeignKey('deal.id'))
    investor_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    amount = db.Column(db.Integer)
    investment_type = db.Column(db.String(255))
    fund_invested = db.Column(db.String(255))
