"""renaming name to name_id

Revision ID: bff566c2bd6b
Revises: 83d2b1915576
Create Date: 2024-12-13 02:42:33.615491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff566c2bd6b'
down_revision = '83d2b1915576'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('ALTER TABLE scholars RENAME COLUMN name TO name_id')


def downgrade() -> None:
    op.execute('ALTER TABLE scholars RENAME COLUMN name_id TO name')