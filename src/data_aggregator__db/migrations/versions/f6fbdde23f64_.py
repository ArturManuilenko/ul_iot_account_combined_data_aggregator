"""empty message

Revision ID: f6fbdde23f64
Revises: 5a54caca6332
Create Date: 2021-08-29 14:48:20.500903

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f6fbdde23f64'
down_revision = '81ceac2cb723'
branch_labels = None
depends_on = None


SERVICE_DEVICE_DB__SYS_USER_ID = "6ff8eaba-b5b4-49b2-9a83-f48fcdf6d361"
SERVICE_DEVICE_DB__SYS__GATEWAY_ID = "e77ea8e3-105b-410d-b383-f0f6a62efca9"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP__ID = "3b0ab436-7357-4041-8533-0b48b41d097d"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP_NCP__ID = "c11e99b9-eaaa-4972-a34f-2303da768ac8"

DEVICE_GATEWAY_NETWORK__NAME__SMP = 'SERVER__UDP__SMP'
DEVICE_GATEWAY_NETWORK__NAME__SMP_NCP = 'SERVER__UDP__SMP_NCP'


def upgrade():
    dt_now = datetime.now()
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP__ID}','{DEVICE_GATEWAY_NETWORK__NAME__SMP}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP_NCP__ID}','{DEVICE_GATEWAY_NETWORK__NAME__SMP_NCP}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")


def downgrade():
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP__ID}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK__SMP_NCP__ID}'")
