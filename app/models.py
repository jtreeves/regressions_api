from app import db
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    key = Column(String(100))
    date = Column(DateTime)

    regressions = relationship('Regression')

class Regression(db.Model):
    __tablename__ = 'regressions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String(100), nullable=False)
    title = Column(String, nullable=False)
    independent = Column(String, nullable=False)
    dependent = Column(String, nullable=False)
    precision = Column(Integer, nullable=False)
    data_set = Column(ARRAY(Float), nullable=False)
    linear_coefficients = Column(ARRAY(Float))
    linear_points = Column(JSON)
    linear_correlation = Column(Float)
    quadratic_coefficients = Column(ARRAY(Float))
    quadratic_points = Column(JSON)
    quadratic_correlation = Column(Float)
    cubic_coefficients = Column(ARRAY(Float))
    cubic_points = Column(JSON)
    cubic_correlation = Column(Float)
    hyperbolic_coefficients = Column(ARRAY(Float))
    hyperbolic_points = Column(JSON)
    hyperbolic_correlation = Column(Float)
    exponential_coefficients = Column(ARRAY(Float))
    exponential_points = Column(JSON)
    exponential_correlation = Column(Float)
    logarithmic_coefficients = Column(ARRAY(Float))
    logarithmic_points = Column(JSON)
    logarithmic_correlation = Column(Float)
    logistic_coefficients = Column(ARRAY(Float))
    logistic_points = Column(JSON)
    logistic_correlation = Column(Float)
    sinusoidal_coefficients = Column(ARRAY(Float))
    sinusoidal_points = Column(JSON)
    sinusoidal_correlation = Column(Float)
    best_fit = Column(String)
    date = Column(DateTime)