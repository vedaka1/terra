"""empty message

Revision ID: 490bdef63ad9
Revises: 
Create Date: 2024-02-08 15:49:03.723424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '490bdef63ad9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='fastapi'
    )
    op.create_index(op.f('ix_fastapi_user_id'), 'user', ['id'], unique=False, schema='fastapi')
    op.create_table('refresh_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.UUID(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['fastapi.user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='fastapi'
    )
    op.create_index(op.f('ix_fastapi_refresh_session_id'), 'refresh_session', ['id'], unique=False, schema='fastapi')
    op.create_index(op.f('ix_fastapi_refresh_session_refresh_token'), 'refresh_session', ['refresh_token'], unique=False, schema='fastapi')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fastapi_refresh_session_refresh_token'), table_name='refresh_session', schema='fastapi')
    op.drop_index(op.f('ix_fastapi_refresh_session_id'), table_name='refresh_session', schema='fastapi')
    op.drop_table('refresh_session', schema='fastapi')
    op.drop_index(op.f('ix_fastapi_user_id'), table_name='user', schema='fastapi')
    op.drop_table('user', schema='fastapi')
    # ### end Alembic commands ###
