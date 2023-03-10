"""criação do autor campo

Revision ID: dcce3ee56831
Revises: 7708364131ff
Create Date: 2023-01-17 21:36:21.287529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dcce3ee56831'
down_revision = '7708364131ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanhas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(length=255), nullable=False))
        batch_op.drop_column('donor')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campanhas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('donor', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('author')

    # ### end Alembic commands ###
