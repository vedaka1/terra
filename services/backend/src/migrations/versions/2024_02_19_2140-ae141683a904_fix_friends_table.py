"""fix friends table

Revision ID: ae141683a904
Revises: c7191e2284b7
Create Date: 2024-02-19 21:40:31.832739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae141683a904'
down_revision: Union[str, None] = 'c7191e2284b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_to_user',
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('friend_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['friend_id'], ['fastapi.user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['fastapi.user.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_to_user')
    # ### end Alembic commands ###