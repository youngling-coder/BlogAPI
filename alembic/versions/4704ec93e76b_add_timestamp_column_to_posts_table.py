"""add timestamp column to posts table

Revision ID: 4704ec93e76b
Revises: 333c4f47db0d
Create Date: 2024-02-12 14:29:26.568954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4704ec93e76b'
down_revision: Union[str, None] = '333c4f47db0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("timestamp", type_=sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "timestamp")
    pass
