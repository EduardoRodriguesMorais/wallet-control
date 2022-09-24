from app.config.settings import get_settings
from neomodel import config


setting = get_settings()


def init_neo4j():
    config.DATABASE_URL = setting.NEO4J_ACCESS
