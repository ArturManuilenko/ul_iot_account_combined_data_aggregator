"""empty message

Revision ID: 610c0fe71413
Revises: c824166e4812
Create Date: 2021-10-30 14:00:06.615087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '610c0fe71413'
down_revision = 'c824166e4812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device_battery',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=False),
    sa.Column('is_alive', sa.Boolean(), nullable=False),
    sa.Column('user_created_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_modified_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('device_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    op.create_table('device_event',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=False),
    sa.Column('is_alive', sa.Boolean(), nullable=False),
    sa.Column('user_created_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_modified_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('device_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('type', sa.Enum('BATTERY_IS_LOW', 'MAGNET_WAS_DETECTED', 'CASE_WAS_OPENED', 'TEMPERATURE_LIMIT', name='integrationv0messageevent'), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    op.create_table('device_temperature',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=False),
    sa.Column('is_alive', sa.Boolean(), nullable=False),
    sa.Column('user_created_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_modified_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('device_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    op.create_table('device_value',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=False),
    sa.Column('is_alive', sa.Boolean(), nullable=False),
    sa.Column('user_created_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_modified_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('device_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('channel', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('device_value')
    op.drop_table('device_temperature')
    op.drop_table('device_event')
    op.drop_table('device_battery')
    # ### end Alembic commands ###
