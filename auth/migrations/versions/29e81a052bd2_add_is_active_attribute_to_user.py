"""Add is_active attribute to User

Revision ID: 29e81a052bd2
Revises: 52e9c6173638
Create Date: 2024-04-18 04:53:41.249606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29e81a052bd2'
down_revision = '52e9c6173638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###