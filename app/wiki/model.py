
from app import db

class WikiPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(1000), index=True)
    title = db.Column(db.String(1000), index=True)
    content = db.Column(db.String(30000), index=True)
    locale = db.Column(db.String(1000), index=True)
    is_visible = db.Column(db.Boolean)

    def __repr__(self):
        return '<WikiPage id: {}, title: {}>'.format(self.id, self.title)

    def to_dict(self):
        wiki_page = {
            'id': self.id,
            'slug': self.slug,
            'title': self.title,
            'content': self.content,
            'locale': self.locale,
            'is_visible': self.is_visible,
        }
        return wiki_page