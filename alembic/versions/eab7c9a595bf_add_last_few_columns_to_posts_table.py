"""add last few columns to posts table

Revision ID: eab7c9a595bf
Revises: 7200a668838a
Create Date: 2022-07-11 15:07:45.118113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab7c9a595bf'
down_revision = '7200a668838a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE')),
    op.add_column("posts", sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
