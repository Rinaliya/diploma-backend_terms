from app import db

class Terms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(1000), index=True)
    definition = db.Column(db.String(1000), index=True)
    locale = db.Column(db.String(1000), index=True)

    def __repr__(self):
        return '<Terms id: {}, title: {}>'.format(self.id, self.title)

    def to_dict(self):
        terms = {
            'id': self.id,
            'term': self.term,
            'definition': self.definition,
            'locale': self.locale,
        }
        return terms