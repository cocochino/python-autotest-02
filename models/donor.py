'''
Created on Aug 18, 2023

@author: Miho
'''
from db import db


class DonorModel(db.Model):
    #__tablename__ = 'items'
    __tablename__ = 'donors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(10))

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def json(self):
        return {'name': self.name, 'type': self.type}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
