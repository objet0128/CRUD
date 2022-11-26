from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from crud.db.base import BaseMixin
from crud.db.base_class import Base


class User(Base, BaseMixin):
    email = Column(String, unique=True, index=True)
    password = Column(String)
    information = Column(String)
    articles = relationship("Article", back_populates="user", lazy="joined")
    comments = relationship("Comment", back_populates="user", lazy="joined")
