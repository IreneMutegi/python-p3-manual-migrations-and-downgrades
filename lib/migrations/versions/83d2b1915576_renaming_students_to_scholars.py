"""Renaming students to scholars

Revision ID: 83d2b1915576
Revises: 791279dd0760
Create Date: 2024-12-13 02:31:10.805679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d2b1915576'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
