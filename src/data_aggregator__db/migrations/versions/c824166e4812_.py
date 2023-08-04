"""empty message

Revision ID: c824166e4812
Revises: f2cce2255e47
Create Date: 2021-09-14 07:27:36.908481

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'c824166e4812'
down_revision = 'f6fbdde23f64'
branch_labels = None
depends_on = None


SERVICE_DEVICE_DB__SYS_USER_ID = "6ff8eaba-b5b4-49b2-9a83-f48fcdf6d361"
SERVICE_DEVICE_DB__SYS__GATEWAY_ID = "e77ea8e3-105b-410d-b383-f0f6a62efca9"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG = "a5981f6b-98cd-4899-8d6d-174a5c5b0b6f"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG = "be1b3408-13c2-43c3-b151-213a662d2fcf"

DEVICE_GATEWAY_NETWORK__NAME_LOG = 'LOGGER'
DEVICE_GATEWAY_NETWORK__NAME_AGG = 'AGGREGATOR'


def upgrade():
    dt_now = datetime.utcnow()
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG}','{DEVICE_GATEWAY_NETWORK__NAME_AGG}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'output'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG}','{DEVICE_GATEWAY_NETWORK__NAME_LOG}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'output'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")


def downgrade():
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG}'")
