from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2025_03_12_01_create_roles_and_auditions'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('character_name', sa.String(length=50), nullable=False)
    )

    # Create auditions table
    op.create_table(
        'auditions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('actor', sa.String(length=50), nullable=False),
        sa.Column('location', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.Integer(), nullable=False),
        sa.Column('hired', sa.Boolean(), nullable=False),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'), nullable=False)
    )

def downgrade():
    op.drop_table('auditions')
    op.drop_table('roles')
