from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from crud.db.base import BaseMixin
from crud.db.base_class import Base


class Comment(Base, BaseMixin):

    comment: str = Column(String(50))
    user_id: int = Column(Integer, ForeignKey("user.id"))
    article_id: int = Column(Integer, ForeignKey("article.id"))
    user = relationship("User", back_populates="comments")
    article = relationship("Article", back_populates="comments")
