"""add user table

Revision ID: 4072b4a18eb7
Revises: 84345aa73862
Create Date: 2024-02-12 14:07:48.019683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4072b4a18eb7'
down_revision: Union[str, None] = '84345aa73862'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", type_=sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("username", type_=sa.String(), nullable=False),
                    sa.Column("password", type_=sa.String(), nullable=False),
                    sa.Column("timestamp", type_=sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("username"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
