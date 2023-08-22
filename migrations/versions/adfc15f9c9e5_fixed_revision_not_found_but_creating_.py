"""fixed revision not found but creating new

Revision ID: adfc15f9c9e5
Revises: adf88201c9bf
Create Date: 2023-08-21 20:50:19.757750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adfc15f9c9e5'
down_revision: Union[str, None] = 'adf88201c9bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caster_deck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caster_deck', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uld',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uld_name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('caster_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caster_id'], ['caster_deck.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uld')
    op.drop_table('flight')
    op.drop_table('caster_deck')
    # ### end Alembic commands ###
