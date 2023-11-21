"""empty message

Revision ID: 13c9e9ef6dec
Revises: 
Create Date: 2023-11-20 15:30:05.004951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c9e9ef6dec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.Integer(), nullable=False),
    sa.Column('recipe_title', sa.String(length=120), nullable=False),
    sa.Column('recipe_image', sa.String(length=200), nullable=False),
    sa.Column('recipe_servings', sa.Integer(), nullable=False),
    sa.Column('recipe_prep_time', sa.Integer(), nullable=False),
    sa.Column('recipe_cost', sa.String(length=10), nullable=False),
    sa.Column('recipe_diet', sa.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('external_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('firstName', sa.String(length=80), nullable=True),
    sa.Column('lastName', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('linkedIn', sa.String(length=200), nullable=True),
    sa.Column('github', sa.String(length=200), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favourite_recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recipe_external_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_external_id'], ['recipe.external_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourite_recipes')
    op.drop_table('user')
    op.drop_table('recipe')
    # ### end Alembic commands ###
