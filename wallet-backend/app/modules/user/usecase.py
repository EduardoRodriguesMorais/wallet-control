import uuid

from decouple import config
from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT
from passlib.hash import pbkdf2_sha256
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.core.message_enum import MessageEnum
from app.modules.core.utils import (
    valid_email,
    valid_name,
    valid_password,
)
from app.modules.user import repository, schema
from app.modules.user.model import User
from app.modules.core.graph_models import User as UserNode, Spent


class GetUserService:
    def __init__(self, id: int):
        self._id = id
        self._repository = repository.UserRepository()

    async def _validate(self):
        user = await self._repository.get_by_id(self._id)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessageEnum.EMAIL_ALREADY_EXISTS.value,
            )
        return user

    async def execute(self):
        user = await self._validate()
        return schema.GetUserSchema().from_orm(user)


class GetUsersService:
    def __init__(self):
        self._repository = repository.UserRepository()
        self._pydantic_model = pydantic_model_creator(User)

    async def _serializer(self, user):
        result = await self._pydantic_model.from_tortoise_orm(user)
        return schema.GetUserSchema(**result.dict())

    async def execute(self):
        users = await self._repository.get_all()
        return [await self._serializer(user) for user in users]


class CreateUserService:
    def __init__(self, payload: schema.PostUserSchema):
        self._payload = payload
        self._repository = repository.UserRepository()
        self._pydantic_model = pydantic_model_creator(User)

    async def _validate_user(self):
        valid_name(self._payload.name)
        valid_email(self._payload.email)
        valid_password(self._payload.password)
        user = await self._repository.get_by_email(self._payload.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessageEnum.EMAIL_ALREADY_EXISTS.value,
            )

    async def _create_node(self, user: User):
        node = UserNode(uuid=uuid.uuid4().hex, name=user.name, email=user.email)
        node.save()
        return node

    async def _relating_node(self, user_node: UserNode):
        spending_base = Spent().nodes.filter(base=True)
        for spent_node in spending_base:
            spent_node.user.connect(user_node)

    async def execute(self):
        await self._validate_user()
        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        dict_user = self._payload.dict()
        user = await self._repository.create(dict_user)
        user_node = await self._create_node(user)
        await self._relating_node(user_node)
        result = await self._pydantic_model.from_tortoise_orm(user)
        return schema.GetUserSchema(**result.dict())


class LoginService:
    def __init__(self, payload: schema.PostUserEmailPasswordSchema, authorize: AuthJWT):
        self._payload = payload
        self._repository = repository.UserRepository()
        self._authorize = authorize

    async def _validate(self):
        user = await self._repository.get_by_email(self._payload.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessageEnum.USER_NOT_FOUND.value,
            )

        return user

    async def _serializer(self, user):
        access_token = self._authorize.create_access_token(subject=user.id)
        return {
            "email": user.email,
            "access_token": access_token,
        }

    async def execute(self):
        user = await self._validate()
        if not pbkdf2_sha256.verify(self._payload.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessageEnum.USER_INVALID_PASSWORD.value,
            )
        user_serialized = await self._serializer(user)
        return schema.JWTUserSchema(**user_serialized)


class CreateUserAdminService:
    def __init__(self):
        self._repository = repository.UserRepository()
        self._pydantic_model = pydantic_model_creator(User)
        self._create_admin_user = config("CREATE_ADMIN", default=False, cast=bool)

    async def _validate(self):
        if self._create_admin_user and not await self._repository.get_by_email(
            config("EMAIL_ADMIN")
        ):
            return schema.PostUserSchema(
                email=config("EMAIL_ADMIN"),
                name=config("NAME_ADMIN"),
                password=pbkdf2_sha256.hash(config("PASSWORD_ADMIN")),
            ).dict()
        return None

    async def execute(self):
        user_dict = await self._validate()
        if user_dict:
            user_dict["email_is_valid"] = True
            await self._repository.create(user_dict)
