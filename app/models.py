from app import db
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    key = Column(String(100))
    regressions = relationship('Regression')

    def __repr__(self):
        return f'<User {self.id}>'    

class Regression(db.Model):
    __tablename__ = 'regression'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
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

    def __repr__(self):
        return f'<Regression {self.id}>'