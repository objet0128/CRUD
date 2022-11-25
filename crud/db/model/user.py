from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from crud.db.base import BaseMixin
from crud.db.base_class import Base


class User(Base, BaseMixin):
    email: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    information: str = Column(String)
    articles = relationship("Article", back_populates="user", lazy="joined")
    comments = relationship("Comment", back_populates="user", lazy="joined")
