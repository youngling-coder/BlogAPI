"""create posts table

Revision ID: d9a3a387a939
Revises:
Create Date: 2024-02-12 13:49:13.073335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9a3a387a939'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", type_=sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", type_=sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
