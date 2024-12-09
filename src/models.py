import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): 
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True) 
    username = Column(String(40), unique=True, nullable=False) 
    email = Column(String(40), unique=True, nullable=False) 
    password = Column(String(80), nullable=False) 
    firstname = Column(String(50)) 
    lastname = Column(String(50)) 
     
    favorites = relationship('Favorite', back_populates='user')
    
class Planet(Base):
     __tablename__ = 'planet' 
     id = Column(Integer, primary_key=True) 
     name = Column(String(30), unique=True, nullable=False) 
     climate = Column(String(30)) 
     terrain = Column(String(30)) 
     population = Column(Integer(30)) 

     favorites = relationship('Favorite', back_populates='planet') 
     
class Character(Base): 
    __tablename__ = 'character' 
    id = Column(Integer, primary_key=True) 
    name = Column(String(40), unique=True, nullable=False) 
    species = Column(String(40)) 
    homeworld = Column(String(40)) 
    affiliation = Column(String(40)) 

    favorites = relationship('Favorite', back_populates='character') 
     
class Favorite(Base):
     __tablename__ = 'favorite' 
     id = Column(Integer, primary_key=True) 
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
     planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True) 
     character_id = Column(Integer, ForeignKey('character.id'), nullable=True) 
     
     user = relationship('User', back_populates='favorites') 
     planet = relationship('Planet', back_populates='favorites') 
     character = relationship('Character', back_populates='favorites')



def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
