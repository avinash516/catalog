import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
Base = declarative_base()


class Userdata(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    picture = Column(String(249))

    @property
    def serialize(self):
        # Object in simple serializeable format
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            'picture': self.picture,
        }


class Brands(Base):
    # This class is to create brand table,
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(50), nullable=False)

    user = relationship(Userdata, backref="brands")

    @property
    def serialize(self):
        # Return data as object in simple serializeable format
        return {
            'name': self.name,
            'id': self.id,

        }


class Models(Base):
    # This class is to create model table
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    modelnumber = Column(String(30))
    colors = Column(String(30))

    price = Column(String(20))
    description = Column(String(500))

    brands = relationship(Brands, backref=backref('models',
                          cascade='all, delete'))
    users = relationship(Userdata, backref="models")

    @property
    def serialize(self):
        # Return data as object in simple serializeable format
        return {

            'id': self.id,

            'modelnumber': self.modelnumber,

            'colors':  self.colors,
            'price': self.price,
            'description': self.description,


        }

engine = create_engine('sqlite:///shoes.db')
Base.metadata.create_all(engine)
