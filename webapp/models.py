import datetime

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
    time = db.Column(db.DateTime())
    speaker_id = db.Column(db.Integer(), db.ForeignKey('speaker.id'))
    description = db.Column(db.Text())

