from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import BaseMixin
from app.models.articles import Article


class User(Base, BaseMixin):

    email = Column(String, unique=True, index=True)
    password = Column(String)
    information = Column(String)
    article = relationship("Article", back_populates="user")
