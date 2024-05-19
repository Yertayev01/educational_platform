"""comment

Revision ID: 00baae8ebd4e
Revises:
Create Date: 2024-05-18 21:19:03.854036

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "00baae8ebd4e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the 'users' table
    op.create_table(
        "users",
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False, unique=True),
        sa.Column("is_active", sa.Boolean(), default=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("roles", sa.ARRAY(sa.String()), nullable=False),
    )


def downgrade() -> None:
    # Drop the 'users' table
    op.drop_table("users")
