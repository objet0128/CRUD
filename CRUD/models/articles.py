from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from CRUD.db.base_class import Base
from CRUD.models.base import BaseMixin


class Article(Base, BaseMixin):

    title = Column(String(50))
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="articles")
    comments = relationship("Comment", back_populates="article")
