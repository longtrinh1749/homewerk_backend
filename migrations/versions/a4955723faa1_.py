"""empty message

Revision ID: a4955723faa1
Revises: a136f0472adb
Create Date: 2022-04-27 13:52:46.860966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4955723faa1'
down_revision = 'a136f0472adb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignments', sa.Column('instruction', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignments', 'instruction')
    # ### end Alembic commands ###
