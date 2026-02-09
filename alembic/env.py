from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# -------------------------------------------------
# Alembic Config object
# -------------------------------------------------
config = context.config

# Set up Python logging from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -------------------------------------------------
# IMPORT YOUR APP STUFF HERE
# -------------------------------------------------
from app.database import Base
from app import models  # IMPORTANT: registers all models
from app.config import DATABASE_URL

# This is what Alembic uses to detect schema changes
target_metadata = Base.metadata

# -------------------------------------------------
# OFFLINE MIGRATIONS
# -------------------------------------------------
def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    This does NOT connect to the database.
    It just generates SQL.
    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# -------------------------------------------------
# ONLINE MIGRATIONS
# -------------------------------------------------
def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.
    This DOES connect to the database.
    """
    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# -------------------------------------------------
# ENTRY POINT
# -------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
