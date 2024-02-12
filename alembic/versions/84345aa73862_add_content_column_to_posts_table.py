"""Add content column to posts table

Revision ID: 84345aa73862
Revises: d9a3a387a939
Create Date: 2024-02-12 13:59:06.004301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84345aa73862'
down_revision: Union[str, None] = 'd9a3a387a939'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", type_=sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
