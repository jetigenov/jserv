# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, Column


db = SQLAlchemy()
Base = db.Model


class Question(Base):
    __tablename__ = 't_question'
    __table_args__ = {'schema': 'core'}

    id = Column(Integer, primary_key=True)
    question = Column(String(16))
    answer = Column(String(16))
    date_create = Column(DateTime)
