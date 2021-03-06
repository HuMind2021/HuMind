"""empty message

Revision ID: 3f53491a1657
Revises: 
Create Date: 2021-02-22 14:42:24.605823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f53491a1657'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('_password', sa.VARCHAR(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('facebook', sa.VARCHAR(), nullable=True),
    sa.Column('instagram', sa.VARCHAR(), nullable=True),
    sa.Column('twitter', sa.VARCHAR(), nullable=True),
    sa.Column('linkedIn', sa.VARCHAR(), nullable=True),
    sa.Column('youTube', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_psychologist', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.VARCHAR(), nullable=True),
    sa.Column('company_number', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_number')
    )
    op.create_table('user_psychologist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('identity_number', sa.VARCHAR(), nullable=True),
    sa.Column('association_number', sa.VARCHAR(), nullable=True),
    sa.Column('speciality', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('association_number'),
    sa.UniqueConstraint('identity_number')
    )
    op.create_table('search_workshop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('duration', sa.VARCHAR(), nullable=True),
    sa.Column('max_price', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('max_people', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user_company_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_company_id'], ['user_company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workshop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('duration', sa.VARCHAR(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('max_people', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_psychologist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_psychologist_id'], ['user_psychologist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workshop_has_category',
    sa.Column('workshop_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['workshop_id'], ['workshop.id'], ),
    sa.PrimaryKeyConstraint('workshop_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workshop_has_category')
    op.drop_table('workshop')
    op.drop_table('search_workshop')
    op.drop_table('user_psychologist')
    op.drop_table('user_company')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
