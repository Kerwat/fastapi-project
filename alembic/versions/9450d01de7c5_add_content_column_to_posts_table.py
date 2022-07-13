"""add content column to posts table

Revision ID: 9450d01de7c5
Revises: 1f1757c155ec
Create Date: 2022-07-11 14:30:44.390617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9450d01de7c5'
down_revision = '1f1757c155ec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
