"""empty message

Revision ID: 719e17a13174
Revises: 9eb0b47e1216
Create Date: 2022-04-30 20:09:49.833373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '719e17a13174'
down_revision = '9eb0b47e1216'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('works', sa.Column('active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('works', 'active')
    # ### end Alembic commands ###
