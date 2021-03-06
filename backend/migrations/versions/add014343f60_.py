"""empty message

Revision ID: add014343f60
Revises: a082b396b244
Create Date: 2020-09-02 21:10:08.361982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add014343f60'
down_revision = 'a082b396b244'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('date_created', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'date_created')
    # ### end Alembic commands ###
