from alembic import context
from lib.models import Base
from sqlalchemy import create_engine

# Add your model's MetaData object here
target_metadata = Base.metadata

# Directly set the database URL
engine = create_engine("sqlite:///theater.db")  # Update with your actual database URL

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations():
    """Run migrations based on the context mode."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()

if __name__ == "__main__":
    run_migrations()
