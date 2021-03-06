"""empty message

Revision ID: 76079b6fb8dc
Revises: 9ae2ff2a5e76
Create Date: 2022-05-25 15:12:52.456345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
import homewerk

revision = '76079b6fb8dc'
down_revision = '9ae2ff2a5e76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('scope', sa.String(length=255), nullable=False),
    sa.Column('path', sa.Integer(), nullable=False),
    sa.Column('trigger_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', homewerk.models.base.BaseTimestamp(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', homewerk.models.base.BaseTimestamp(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    # ### end Alembic commands ###
