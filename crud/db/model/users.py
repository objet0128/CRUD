import re

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, validates

from crud.db.base import BaseMixin
from crud.db.base_class import Base


class User(Base, BaseMixin):
    email = Column(String, unique=True, index=True)
    password = Column(String)
    information = Column(String)
    articles = relationship("Article", back_populates="user")
    comments = relationship("Comment", back_populates="user")

    @validates("email")
    def validate_email(self, key, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Only email please")
        else:
            return value
