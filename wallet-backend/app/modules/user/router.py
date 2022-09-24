from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate

from app.config.settings import get_settings
from app.modules.core.logging import LoggingUnder
from app.modules.user import schema, usecase

router = APIRouter()
setting = get_settings()


@router.get(
    "/",
    description="Router to list all users registered",
    response_model=Page[schema.GetUserSchema],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(LoggingUnder())],
)
async def get_users():
    users = await usecase.GetUsersService().execute()
    return paginate(users)


@router.get(
    "/{id}",
    description="Router to one user by id",
    response_model=schema.GetUserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(LoggingUnder())],
)
async def get_user(id: int):
    return await usecase.GetUserService(id).execute()


@router.post(
    "/",
    description="This router is to create new user",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(LoggingUnder())],
)
async def post_user(payload: schema.PostUserSchema):
    return await usecase.CreateUserService(payload).execute()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=schema.JWTUserSchema,
    description="This router is to login user",
    dependencies=[Depends(LoggingUnder())],
)
async def login(
    payload: schema.PostUserEmailPasswordSchema, authorize: AuthJWT = Depends()
):
    return await usecase.LoginService(payload, authorize).execute()


@router.post(
    "/create-admin",
    status_code=status.HTTP_201_CREATED,
    description="This router is to create admin user",
)
async def create_admin():
    await usecase.CreateUserAdminService().execute()
    return {"detail": "Admin user created"}
