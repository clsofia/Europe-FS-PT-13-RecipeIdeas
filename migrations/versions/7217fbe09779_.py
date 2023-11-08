"""empty message

Revision ID: 7217fbe09779
Revises: bc0272c8c7fc
Create Date: 2023-11-08 19:42:21.201775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7217fbe09779'
down_revision = 'bc0272c8c7fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstName', sa.String(length=80), nullable=True))
        batch_op.add_column(sa.Column('lastName', sa.String(length=80), nullable=True))
        batch_op.add_column(sa.Column('userName', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('userName')
        batch_op.drop_column('lastName')
        batch_op.drop_column('firstName')

    # ### end Alembic commands ###
