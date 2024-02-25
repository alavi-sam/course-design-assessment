"""empty message

Revision ID: 91cc23693308
Revises: 9de25f3d4b2b
Create Date: 2024-02-25 01:27:57.612712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '91cc23693308'
down_revision: Union[str, None] = '9de25f3d4b2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('student_name', sa.String(length=50), nullable=False))
    op.drop_column('student', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('student', 'student_name')
    # ### end Alembic commands ###
