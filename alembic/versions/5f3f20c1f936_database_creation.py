"""Database creation

Revision ID: 5f3f20c1f936
Revises: 
Create Date: 2023-07-25 17:15:21.876704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3f20c1f936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_description',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('description', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['description'], ['product_description.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('product_description')
    # ### end Alembic commands ###
