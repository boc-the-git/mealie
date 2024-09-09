"""'Add timer to recipe_instructions'

Revision ID: f2a073082c28
Revises: 32d69327997b
Create Date: 2024-08-18 11:30:16.566883

"""

import sqlalchemy as sa
from sqlalchemy import orm

from alembic import op

# revision identifiers, used by Alembic.
revision = "f2a073082c28"
down_revision = "32d69327997b"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("recipe_instructions", schema=None) as batch_op:
        batch_op.add_column(sa.Column("timer", sa.Integer(), nullable=True))

    bind = op.get_bind()
    session = orm.Session(bind=bind)

    with session:
        stmt = "UPDATE recipe_instructions SET timer = 10;"

        session.execute(sa.text(stmt))


def downgrade():
    with op.batch_alter_table("recipe_instructions", schema=None) as batch_op:
        batch_op.drop_column("timer")
