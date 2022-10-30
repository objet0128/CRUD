from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import BaseMixin


class Comment(Base, BaseMixin):

    comment = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    article_id = Column(Integer, ForeignKey("article.id"))
    user = relationship("User", back_populates="comments")
    article = relationship("Article", back_populates="comments")