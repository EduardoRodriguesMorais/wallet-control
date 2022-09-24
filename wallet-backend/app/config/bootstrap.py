from fastapi import FastAPI
from loguru import logger

from app.config.db import close_connection_database, connect_to_database, init_db
from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.neo4j import init_neo4j
from app.config.routers import init_routers
from app.config.settings import get_settings

setting = get_settings()

logger.remove(0)


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=setting.APP_NAME,
        version=setting.APP_VERSION,
        description=setting.APP_DESCRIPTION,
        root_path=setting.ROOT_PATH,
    )

    init_db(application)
    init_routers(application)
    init_middlewares(application)
    exception_jwt(application)
    init_jwt()
    init_neo4j()

    return application


app = create_app()


@app.on_event("startup")
async def statup_event():
    logger.info("Starting up...")
    await connect_to_database()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()
