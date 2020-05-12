from app import db
from datetime import datetime


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    stargazers = db.Column(db.BigInteger, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Lang {}>'.format(self.name)
