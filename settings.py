"""File with settings and configs for the project"""
from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/fastapi_prod",
)  # connect string for the real database
APP_PORT = env.int("APP_PORT", default=8010)

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
SENTRY_URL: str = env.str(
    "SENTRY_URL",
    default="https://9b031e74450e0125f25d3b2ea0d59a9d@o4507276533039104.ingest.us.sentry.io/4507276534939648",
)

# test envs
TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres",
)  # connect string for the test database
