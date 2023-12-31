"""removed associations to uld and caster

Revision ID: a1a21693929e
Revises: 4c849ee69510
Create Date: 2023-08-22 17:11:34.458471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1a21693929e'
down_revision: Union[str, None] = '4c849ee69510'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uld_caster')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uld_caster',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('uld_id', sa.INTEGER(), nullable=True),
    sa.Column('caster_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['caster_id'], ['caster_deck.id'], ),
    sa.ForeignKeyConstraint(['uld_id'], ['uld.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
