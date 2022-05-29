"""empty message

Revision ID: 7e04eef0aa0e
Revises: f9f55f3ade43
Create Date: 2022-05-29 18:34:34.939696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e04eef0aa0e'
down_revision = 'f9f55f3ade43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('saved', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('saved', 'description')
    # ### end Alembic commands ###
