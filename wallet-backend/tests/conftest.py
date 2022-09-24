import pytest
from faker import Factory
from starlette.testclient import TestClient
from tortoise.contrib.starlette import register_tortoise

from app.config.db import settings
from app.config.settings import Setting, get_settings
from app.main import create_app

setting = get_settings()
faker = Factory.create("pt_BR")


def get_settings_overide():
    return Setting(TESTING=True, DB_URL=setting.DB_TEST_URL)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_overide
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_overide
    register_tortoise(
        app,
        db_url=setting.DB_TEST_URL,
        modules={"models": setting.MODELS},
        generate_schemas=True,
    )
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def access_token(test_app_with_db):
    user_admin = test_app_with_db.post("/users/create-admin")
    response = test_app_with_db.post(
        "/users/login",
        json={"email": settings.EMAIL_ADMIN, "password": settings.PASSWORD_ADMIN},
    )

    payload = response.json()

    return {"Authorization": f"Bearer {payload['accessToken']}"}
