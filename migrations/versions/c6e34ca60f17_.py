"""empty message

Revision ID: c6e34ca60f17
Revises: 719e17a13174
Create Date: 2022-05-01 22:18:38.374137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6e34ca60f17'
down_revision = '719e17a13174'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('work_objects', sa.Column('value', sa.String(255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('work_objects', 'value')
    # ### end Alembic commands ###