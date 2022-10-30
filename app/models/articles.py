from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import BaseMixin


class Article(Base, BaseMixin):

    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    article_id = Column(Integer, ForeignKey("article.id"))
    user = relationship("User", back_populates="articles")
    comments = relationship("Comment", back_populates="article")
