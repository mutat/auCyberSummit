import datetime
from webapp.extensions import bcrypt
from flask_login import AnonymousUserMixin


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Speaker(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    f_name = db.Column(db.String(255))
    l_name = db.Column(db.String(255))
    image = db.Column(db.String(500))
    employer = db.Column(db.String(255))
    bio = db.Column(db.Text())
    event_sessions = db.relationship(
        'EventSession',
        backref='speaker',
        lazy='dynamic'
    )


class EventSession(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    time = db.Column(db.DateTime())
    speaker_id = db.Column(db.Integer(), db.ForeignKey('speaker.id'))
    description = db.Column(db.Text())


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))


    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
         return True

    def is_anonymous(self):
         if isinstance(self, AnonymousUserMixin):
             return True
         else:
             return False

    def get_id(self):
         return unicode(self.id)

class Poi(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    addr1 = db.Column(db.String(255))
    city = db.Column(db.String(125))
    state = db.Column(db.String(3))
    zip = db.Column(db.String(10))
    description = db.Column(db.Text())
