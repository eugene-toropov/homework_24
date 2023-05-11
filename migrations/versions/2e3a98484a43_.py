"""empty message

Revision ID: 2e3a98484a43
Revises: 
Create Date: 2023-05-12 00:31:22.643971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e3a98484a43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('users')
