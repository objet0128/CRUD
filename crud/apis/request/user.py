import re

from pydantic import BaseModel, validator


class UserCreateDTO(BaseModel):
    email: str
    password: str
    information: str

    @validator("email")
    def validate_email(cls, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Only email please")
        else:
            return value
