"""empty message

Revision ID: bccdb462c715
Revises: 2a99c5699de8
Create Date: 2022-06-11 19:41:51.322194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bccdb462c715'
down_revision = '2a99c5699de8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification_subcriber', sa.Column('read', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notification_subcriber', 'read')
    # ### end Alembic commands ###
