from app import db
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    key = Column(String(100))
    date = Column(DateTime)
    regressions = relationship('Regression')

    # @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'key': self.key,
            'date': self.date
        }

    def __repr__(self):
        return f'<User {self.id}>'    

class Regression(db.Model):
    __tablename__ = 'regressions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    independent = Column(ARRAY(Float))
    dependent = Column(ARRAY(Float))
    linear_coefficients = Column(ARRAY(Float))
    linear_error = Column(ARRAY(Float))
    quadratic_coefficients = Column(ARRAY(Float))
    quadratic_error = Column(Float)
    cubic_coefficients = Column(ARRAY(Float))
    cubic_error = Column(Float)
    hyperbolic_coefficients = Column(ARRAY(Float))
    hyperbolic_error = Column(Float)
    exponential_coefficients = Column(ARRAY(Float))
    exponential_error = Column(Float)
    logarithmic_coefficients = Column(ARRAY(Float))
    logarithmic_error = Column(Float)
    best_fit = Column(String)
    date = Column(DateTime)

    def __repr__(self):
        return f'<Regression {self.id}>'