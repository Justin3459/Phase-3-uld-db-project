"""add caster deck id to repr

Revision ID: db420c0e39ed
Revises: 9ca0e413a655
Create Date: 2023-08-24 13:18:32.874066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db420c0e39ed'
down_revision: Union[str, None] = '9ca0e413a655'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
