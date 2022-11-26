from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from crud.db.base import BaseMixin
from crud.db.base_class import Base


class Article(Base, BaseMixin):

    title = Column(String(50))
    content = Column(String(255))
    author_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="articles")
    comments = relationship("Comment", back_populates="article", lazy="joined")
