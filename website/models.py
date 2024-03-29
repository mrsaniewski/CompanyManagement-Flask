from asyncio import Task

from flask import Flask
from sqlalchemy import Column, String

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    data = db.Column(db.String(10000))
    complete = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    value = db.Column(db.Integer, default=20)
    claimed = db.Column(db.Boolean, default=False)
    first_name = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    points = db.Column(db.Integer, default=0)
    tasks = db.relationship('Task')
    prizes = db.relationship('Prize')
