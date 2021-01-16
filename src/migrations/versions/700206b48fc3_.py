"""empty message

Revision ID: 700206b48fc3
Revises: 9c63e2c91afb
Create Date: 2021-01-16 10:28:43.615756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700206b48fc3'
down_revision = '9c63e2c91afb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_movies_index', table_name='movies')
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    op.create_index('ix_movies_index', 'movies', ['index'], unique=False)
    # ### end Alembic commands ###
