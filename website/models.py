from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
                        db.Column('user.id', db.Integer,
                        db.ForeignKey('user.id')),
                        db.Column('role_id', db.Integer,
                        db.ForeignKey('roles.id'))
                       )

def __repr__(self):
    return f'<Tag id: {self.id}, title: {self.title}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    active = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post', backref='user', passive_deletes=True)

class Role(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    text1 = db.Column(db.Text, nullable=False)
    text2 = db.Column(db.Text, nullable=False)
    text3 = db.Column(db.Text, nullable=False)
    text4 = db.Column(db.Text, nullable=False)
    text5 = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


