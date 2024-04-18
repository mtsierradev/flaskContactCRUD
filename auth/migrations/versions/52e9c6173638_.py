"""empty message

Revision ID: 52e9c6173638
Revises: 8a48821e8035
Create Date: 2024-04-18 04:00:28.228959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52e9c6173638'
down_revision = '8a48821e8035'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.drop_table('people')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('pid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('job', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    op.drop_table('users')
    # ### end Alembic commands ###