"""rename pickle_path to pickle_filename

Revision ID: de5e17d0c54c
Revises: b45ada00516d
Create Date: 2020-11-22 02:01:37.172131

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = 'de5e17d0c54c'
down_revision = 'b45ada00516d'
branch_labels = None
depends_on = None

Session = sessionmaker()


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute("ALTER TABLE ml_model RENAME COLUMN pickle_path TO pickle_filename;")
    session.commit()


def downgrade():
    pass
