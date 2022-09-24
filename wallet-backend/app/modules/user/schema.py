from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class JWTUserSchema(CamelModel):
    email: str
    access_token: str


class GetUserSchema(CamelModel):
    id: int
    name: str
    email: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PostUserSchema(CamelModel):
    name: str = "João Carlos Teste"
    email: str = "joao.teste@email.com"
    password: str = "Teste@123"


class PostUserEmailPasswordSchema(CamelModel):
    email: str = "joao.teste@email.com"
    password: str = "Teste@123"
