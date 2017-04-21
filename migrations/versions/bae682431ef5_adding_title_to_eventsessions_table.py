"""adding title to EventSessions table

Revision ID: bae682431ef5
Revises: 6fb7822def07
Create Date: 2017-04-19 13:20:52.055821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bae682431ef5'
down_revision = '6fb7822def07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event_session', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event_session', 'title')
    # ### end Alembic commands ###