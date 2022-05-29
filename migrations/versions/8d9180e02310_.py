"""empty message

Revision ID: 8d9180e02310
Revises: 7e04eef0aa0e
Create Date: 2022-05-29 18:47:01.837638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d9180e02310'
down_revision = '7e04eef0aa0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('saved', 'path',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('saved', 'path',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###