"""create employees table

Revision ID: 8813deb3c237
Revises:
Create Date: 2026-09-05 13:12:20.620522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8813deb3c237"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create employees table."""
    op.create_table(
        "employees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("department", sa.String(length=100), nullable=False),
        sa.Column("designation", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    op.create_index(
        "ix_employees_id",
        "employees",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_employees_email",
        "employees",
        ["email"],
        unique=True,
    )


def downgrade() -> None:
    """Drop employees table."""
    op.drop_index(
        "ix_employees_email",
        table_name="employees",
    )

    op.drop_index(
        "ix_employees_id",
        table_name="employees",
    )

    op.drop_table("employees")