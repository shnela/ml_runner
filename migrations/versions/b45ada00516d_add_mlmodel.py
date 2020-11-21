"""ADD MLModel

Revision ID: b45ada00516d
Revises: 4d9abdd0e3d1
Create Date: 2020-11-21 23:48:52.272510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45ada00516d'
down_revision = '4d9abdd0e3d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ml_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('pickle_path', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model_name'),
    sa.UniqueConstraint('pickle_path')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ml_model')
    # ### end Alembic commands ###
