from CRUD.db.base_class import Base
from CRUD.db.session import engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def drop_db() -> None:
    Base.metadata.drop_app(bind=engine)