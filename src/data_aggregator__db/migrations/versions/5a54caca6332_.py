from alembic import op
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '5a54caca6332'
down_revision = '300ecde38cd2'
branch_labels = None
depends_on = None


SERVICE_DEVICE_DB__SYS_USER_ID = "6ff8eaba-b5b4-49b2-9a83-f48fcdf6d361"
SERVICE_DEVICE_DB__SYS__TYPE_ID = "c8a0811f-24a8-4517-aab8-e227f2b35533"
SERVICE_DEVICE_DB__SYS__MANUFACTURER_ID = "d02f5807-4545-40fd-9f5d-091822d6868f"
SERVICE_DEVICE_DB__SYS__GATEWAY_ID = "e77ea8e3-105b-410d-b383-f0f6a62efca9"
SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP = "f95ec7ef-07bb-4dac-aa26-8bca2e6cfc3b"
SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP_NCP = "6e65e16c-38b1-430f-bb05-e28242af214a"
SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_WATER_5 = "f2aee1b0-8d8f-4800-92bc-b60213cb0df7"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID = "324570cc-aef6-4a05-8989-ee246155bf7d"

DEVICE_GATEWAY__NAME = 'GATEWAY'
DEVICE_GATEWAY_NETWORK__NAME = 'WWW'


DEVICE_GATEWAY__PROTOCOL_SMP = 'SMP'
DEVICE_GATEWAY__PROTOCOL_NCP_SMP = 'NCP_SMP'
DEVICE_GATEWAY__PROTOCOL_WATER_5 = 'WATER_5'

DEVICE_GATEWAY__INTEGRATION_NAMES = ['MTS', 'A1', 'NERO_OLD', 'BECLOUD']



def upgrade():
    dt_now = datetime.utcnow()
    op.execute(
        f"INSERT INTO public.device_manufacturer (id, name, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__MANUFACTURER_ID}','{DEVICE_GATEWAY__INTEGRATION_NAMES[0]}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway (id, name, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{DEVICE_GATEWAY__NAME}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.protocol (id, name, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP}','{DEVICE_GATEWAY__PROTOCOL_SMP}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.protocol (id, name, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP_NCP}','{DEVICE_GATEWAY__PROTOCOL_NCP_SMP}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.protocol (id, name, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_WATER_5}','{DEVICE_GATEWAY__PROTOCOL_WATER_5}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID}','{DEVICE_GATEWAY_NETWORK__NAME}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")


def downgrade():
    op.execute(f"DELETE FROM public.device_manufacturer WHERE id='{SERVICE_DEVICE_DB__SYS__MANUFACTURER_ID}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID}'")
    op.execute(f"DELETE FROM public.data_gateway WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}'")
    op.execute(f"DELETE FROM public.protocol WHERE id='{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP}'")
    op.execute(f"DELETE FROM public.protocol WHERE id='{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_SMP_NCP}'")
    op.execute(f"DELETE FROM public.protocol WHERE id='{SERVICE_DEVICE_DB__SYS__PROTOCOL_ID_WATER_5}'")
