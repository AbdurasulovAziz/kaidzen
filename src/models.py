from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime

from cors.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    created_at = Column(DateTime, default=datetime.now())

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


    created_at = Column(DateTime, default=datetime.now())

class Repetition(Base):
    __tablename__ = 'repetitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    note_id = Column(Integer, ForeignKey('notes.id'))

    created_at = Column(DateTime, default=datetime.now())
