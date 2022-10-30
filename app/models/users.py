from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import BaseMixin


class User(Base, BaseMixin):

    email = Column(String, unique=True, index=True)
    password = Column(String)
    information = Column(String)
    articles = relationship("Article", back_populates="user")
    comments = relationship("Comment", back_populates="user")
