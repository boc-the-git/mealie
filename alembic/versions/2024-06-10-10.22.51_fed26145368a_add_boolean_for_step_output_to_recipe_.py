"""Add boolean for 'step_output' to recipe ingredient

Revision ID: fed26145368a
Revises: 7788478a0338
Create Date: 2024-06-10 10:22:51.564744

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = "fed26145368a"
down_revision = "7788478a0338"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("recipes_ingredients", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("step_output", sa.Boolean(), nullable=True, default=False)
        )

    op.execute(
        "UPDATE recipes_ingredients SET step_output = 0 WHERE step_output IS NULL"
    )


def downgrade():
    op.execute("DELETE FROM recipes_ingredients WHERE step_output = 1")

    with op.batch_alter_table("recipes_ingredients", schema=None) as batch_op:
        batch_op.drop_column("step_output")
