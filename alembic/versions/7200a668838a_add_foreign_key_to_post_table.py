"""add foreign-key to post table

Revision ID: 7200a668838a
Revises: 32fbe6c5b083
Create Date: 2022-07-11 14:56:13.662651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7200a668838a'
down_revision = '32fbe6c5b083'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
