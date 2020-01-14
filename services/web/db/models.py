from .database import db


class User(db.Document):
    nome = db.StringField(required=True, unique=False)
    email = db.StringField(required=True, unique=True)
    telefones = db.ListField(db.StringField(), required=True)

