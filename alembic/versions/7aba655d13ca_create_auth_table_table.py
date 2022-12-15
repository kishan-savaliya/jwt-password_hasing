"""create auth_table table

Revision ID: 7aba655d13ca
Revises: 
Create Date: 2022-12-15 12:22:29.704487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18eacb64ceb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'auth',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    )


def downgrade() -> None:
    pass
