"""add group recipe actions

Revision ID: 7788478a0338
Revises: d7c6efd2de42
Create Date: 2024-04-07 01:05:20.816270

"""

import sqlalchemy as sa

import mealie.db.migration_types
from alembic import op

# revision identifiers, used by Alembic.
revision = "7788478a0338"
down_revision = "d7c6efd2de42"
branch_labels: str | tuple[str, ...] | None = None
depends_on: str | tuple[str, ...] | None = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "recipe_actions",
        sa.Column("id", mealie.db.migration_types.GUID(), nullable=False),
        sa.Column("group_id", mealie.db.migration_types.GUID(), nullable=False),
        sa.Column("action_type", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("url", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("update_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_recipe_actions_action_type"), "recipe_actions", ["action_type"], unique=False)
    op.create_index(op.f("ix_recipe_actions_created_at"), "recipe_actions", ["created_at"], unique=False)
    op.create_index(op.f("ix_recipe_actions_group_id"), "recipe_actions", ["group_id"], unique=False)
    op.create_index(op.f("ix_recipe_actions_title"), "recipe_actions", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_recipe_actions_title"), table_name="recipe_actions")
    op.drop_index(op.f("ix_recipe_actions_group_id"), table_name="recipe_actions")
    op.drop_index(op.f("ix_recipe_actions_created_at"), table_name="recipe_actions")
    op.drop_index(op.f("ix_recipe_actions_action_type"), table_name="recipe_actions")
    op.drop_table("recipe_actions")
    # ### end Alembic commands ###
