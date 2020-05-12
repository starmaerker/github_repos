from app import db


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    stargazers = db.Column(db.BigInteger, index=True)


    def __repr__(self):
        return '<Lang {}>'.format(self.name)