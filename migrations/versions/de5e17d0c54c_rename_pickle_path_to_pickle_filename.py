"""rename pickle_path to pickle_filename

Revision ID: de5e17d0c54c
Revises: b45ada00516d
Create Date: 2020-11-22 02:01:37.172131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de5e17d0c54c'
down_revision = 'b45ada00516d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('ml_model', sa.Column('pickle_filename', sa.String(length=256), nullable=False))
    op.create_unique_constraint(None, 'ml_model', ['pickle_filename'])
    op.drop_column('ml_model', 'pickle_path')


def downgrade():
    pass
