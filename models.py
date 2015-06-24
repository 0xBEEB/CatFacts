from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(40), unique=True)

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __repr__(self):
        return '<User %r>' % self.phone_number


class Message():

    def __init__(self, params):
        self.sid = params.get('Sid', None)
        self.created = params.get('DateCreated', None)
        self.updated = params.get('DateUpdated', None)
        self.sent = params.get('DateSent', None)
        self.account = params.get('AccountSid', None)
        self.from_number = params.get('From', None)
        self.to_number = params.get('To', None)
        self.body = params.get('Body', None)
        self.status = params.get('Status', None)
        self.direction = params.get('Direction', None)


