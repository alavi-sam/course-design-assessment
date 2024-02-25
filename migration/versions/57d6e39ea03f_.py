"""empty message

Revision ID: 57d6e39ea03f
Revises: e69883ab88f4
Create Date: 2024-02-24 18:52:54.732223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57d6e39ea03f'
down_revision: Union[str, None] = 'e69883ab88f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('test', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'test')
    # ### end Alembic commands ###