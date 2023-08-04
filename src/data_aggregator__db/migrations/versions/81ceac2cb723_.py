"""empty message

Revision ID: 81ceac2cb723
Revises: 821eeee12469
Create Date: 2021-10-18 11:21:41.590152

"""
from datetime import datetime

from alembic import op

from src.data_aggregator__db.model.device_modification_type import DeviceModificationTypeEnum


# revision identifiers, used by Alembic.
revision = '81ceac2cb723'
down_revision = '5a54caca6332'
branch_labels = None
depends_on = None


SERVICE_DEVICE_DB__SYS_USER_ID = "6ff8eaba-b5b4-49b2-9a83-f48fcdf6d361"
SERVICE_DEVICE_DB__SYS__MANUFACTURER = (
    ["b8241b1c-9a67-4b31-96d2-cf358d783242", 'NERO'],
)

# id, sys_name, name_en, name_ru
SERVICE__DEVICE_DB__SYS__DEVICE_METERING_TYPE = (
    ['dc510bb3-4697-4265-ae29-94641b219521', 'water', 'Water', 'Вода'],
    ['bf6c31a8-9786-4a92-be06-78d5b60b1a5a', 'gas', 'Gas', 'Газ'],
    ['d7df4a73-366a-420e-a45a-a983849c14e1', 'electricity', 'Electricity', 'Электричество']
)

# id, type, metering_type_id, sys_name, name_en, name_ru
SERVICE_DEVICE_DB__SYS__MODIFICATION_TYPE = (
    ['8297e747-4f88-4187-8762-e132a875fd95', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo1.1", "Fluo 1.1", "Fluo 1.1"],
    ['61cd94f9-9d2c-472a-9325-de5d126685d0', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo1.2", "Fluo 1.2", "Fluo 1.2"],
    ['aef2fbe8-c3d7-4e7f-bf82-1fb54a731080', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo1.3", "Fluo 1.3", "Fluo 1.3"],
    ['a3d3132c-bdf9-48d5-81cc-071dccc615dc', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo1.4", "Fluo 1.4", "Fluo 1.4"],
    ['1559259d-7d90-499b-95ae-c75d4b143899', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo_nbiot", "Fluo NB-IoT", "Fluo NB-IoT"],
    ['1b7136c2-a43e-4270-84b5-d1f338985cdc', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "Belzenner_lora", "Belzenner LoRa", "БелЦЕННЕР LoRa"],
    ['d958cfc0-4864-4b58-81b4-34abcb3455a8', DeviceModificationTypeEnum.smart_meter.value, 'dc510bb3-4697-4265-ae29-94641b219521', "fluo_a", "Fluo A", "Fluo A"],
    ['9cb3add9-ea95-43aa-9e06-00e9a71a64f0', DeviceModificationTypeEnum.modem.value, 'dc510bb3-4697-4265-ae29-94641b219521', "upiter_nbfi", "Upiter NB-Fi", "Юпитер NB-Fi"],
    ['3bcd3bbf-78b3-4f40-8e2d-6aaf86084d60', DeviceModificationTypeEnum.modem.value, 'dc510bb3-4697-4265-ae29-94641b219521', "upiter_nbiot", "Upiter NB-IoT", "Юпитер NB-IoT"],
    ['23571ac8-83f9-4b43-9154-2d0113932f59', DeviceModificationTypeEnum.modem.value, 'dc510bb3-4697-4265-ae29-94641b219521', "upiter_lora", "Upiter LoRa", "Юпитер LoRa"]
)

# id, device_modification_type_id, name
SERVICE_DEVICE_DB__SYS__MODIFICATION = (
    # Flou 1.2 MM 214
    ['1e41502b-754e-41d0-9ada-9aad9539b83f', '61cd94f9-9d2c-472a-9325-de5d126685d0', 'MM214'],
    # Fluo 1.1 MM 210
    ['131af1df-c2c1-446b-92b1-9e12ed0b89e2', '8297e747-4f88-4187-8762-e132a875fd95', 'MM210'],
    # БелЦЕННЕР LoRa MM 218
    ['d7865820-dd3f-4603-aa5a-e6962d8ec552', '1b7136c2-a43e-4270-84b5-d1f338985cdc', 'MM218'],
    # Fluo A MM 217
    ['11275d5d-fd5c-40c9-ae4d-764d734126c2', 'd958cfc0-4864-4b58-81b4-34abcb3455a8', 'MM217'],
    # Юпитер NB-Fi MM 212
    ['87bcfae9-26a7-4e43-b494-52268437faca', '9cb3add9-ea95-43aa-9e06-00e9a71a64f0', 'MM212'],
    # Юпитер NB-IoT MM 219
    ['2c4e467c-d041-4fcc-b7b2-b3cf5aa1204e', '3bcd3bbf-78b3-4f40-8e2d-6aaf86084d60', 'MM219'],
    # Юпитер LoRa MM216
    ['b51e709c-a755-482e-b069-7a6033d5ad11', '23571ac8-83f9-4b43-9154-2d0113932f59', 'MM216'],
)

SERVICE_DEVICE_DB__SYS__GATEWAY_ID = "e77ea8e3-105b-410d-b383-f0f6a62efca9"

DEVICE_GATEWAY_NETWORK__NAME_OLD = "OLD_LK"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD = "98c028d6-f71b-407b-ad70-02e805e6fb86"
DEVICE_GATEWAY_NETWORK__NAME_SMP = "UDP__SMP"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP = "4e719da0-1814-4075-9cd3-202826e917e9"
DEVICE_GATEWAY_NETWORK__NAME_SMP_NCP = "UDP__NCP_SMP"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP_NCP = "97759efa-bb85-463d-b198-64f60e6492e7"

SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG = "a5981f6b-98cd-4899-8d6d-174a5c5b0b6f"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG = "be1b3408-13c2-43c3-b151-213a662d2fcf"
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG_OUTPUT = '62ce4cbe-9018-49a0-a843-c686325e96b7'
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG_OUTPUT = '62db1e32-2ab4-4144-8dfc-93f6178880a0'
SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD_LK_OUTPUT = '10ccf1b2-402e-4cdb-95e2-62d7dc379055'
DEVICE_GATEWAY_NETWORK__NAME_OUTPUT = ["integration_data_logger", "integration_data_aggregator", "integration_old_nero_lk"]


# later
# SERVICE_DEVICE_DB__SYS__FIRMWARE_ID = [
#     'd1e29066-4a61-4eb3-b10b-fd6f2959d290',
#     '851d1114-1492-4500-b65d-397ec4ec3c3d',
#     '8d57b62d-15f7-437c-98b5-2a58ca385439',
#     'a74a2aca-711c-488c-8483-5861587daebe',
#     '2ffd8640-ad02-4b51-9ef6-38c93f1f99fa',
#     '45653cee-886d-4e34-9c71-954c7a93ff14',
#     '9ed2cc03-8d9c-475b-b13a-1efdef930c1b',
#     'c5b6b83c-ff70-4bc9-bfdb-0b402f42da33',
#     'd1aa472a-323e-47be-9f8d-8b19aaa6ffb2',
#     'd7efab81-cb22-4521-9815-200b2ac39701',
# ]

# SERVICE_DEVICE_DB__SYS__FIRMWARE_UPGRADE_PLAN_ID = [
# 'c37f6463-0ab8-4337-a102-59ceba55ffc2',
# '1a5370bf-b48b-4b2f-aa09-241c038f9d6f',
# '6a89a673-c849-452a-a298-7cc61acac55b',
# 'ee9a0696-e6ad-428a-afa6-f8bd6cfc2c6e',
# '0949060a-4420-4767-9d75-4d1be2200414',
# '59caa45f-227f-4c10-b753-103243dcc0ab',
# '54a91e59-1540-4307-9684-5d441e7b982c',
# 'c7c79b75-5f6c-45f9-8a52-2665111e484b',
# '9c05afc8-7fde-40a4-bd55-43dd093523b4',
# 'bb354d95-b988-40f5-b8f3-e7fa2eb5bdd5',
# ]

# SERVICE_DEVICE_DB__SYS__FIRMWARE_VERSION = [
#     '133.18.1.4',
#     '133.15.2.4',
#     '133.13.2.4',
#     '133.15.1.4',
#     '133.14.1.4',
#     '133.13.1.4',
#     '134.2.2.2',
#     '133.18.2.4',
#     '133.16.2.4',
#     '133.17.2.4',
# ]

def upgrade():
    dt_now = datetime.utcnow()
    for id, name in SERVICE_DEVICE_DB__SYS__MANUFACTURER:
        op.execute(
            f"INSERT INTO public.device_manufacturer "\
            "(id, name, date_created, date_modified, user_created_id, user_modified_id, is_alive)"
            f"VALUES ('{id}','{name}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    for id, sys_name, name_en, name_ru in SERVICE__DEVICE_DB__SYS__DEVICE_METERING_TYPE:
        op.execute(
            f"INSERT INTO public.device_metering_type " \
            "(id, date_created, date_modified, user_created_id, user_modified_id, is_alive, " \
            "sys_name, name_ru, name_en) " \
            f"VALUES ('{id}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True, " \
            f"'{sys_name}','{name_ru}','{name_en}')")
    for id, type, metering_type_id, sys_name, name_en, name_ru in SERVICE_DEVICE_DB__SYS__MODIFICATION_TYPE:
        op.execute(
            f"INSERT INTO public.device_modification_type " \
            "(id, date_created, date_modified, user_created_id, user_modified_id, is_alive, " \
            "type, metering_type_id, sys_name, name_ru, name_en) " \
            f"VALUES ('{id}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True, " \
            f"'{type}', '{metering_type_id}', '{sys_name}','{name_ru}','{name_en}')")
    for id, device_modification_type_id, name in SERVICE_DEVICE_DB__SYS__MODIFICATION:
        op.execute(
            f"INSERT INTO public.device_modification " \
            "(id, date_created, date_modified, user_created_id, user_modified_id, is_alive, " \
            "device_modification_type_id, name) " \
            f"VALUES ('{id}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True, " \
            f"'{device_modification_type_id}', '{name}')")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD}','{DEVICE_GATEWAY_NETWORK__NAME_OLD}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP}','{DEVICE_GATEWAY_NETWORK__NAME_SMP}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP_NCP}','{DEVICE_GATEWAY_NETWORK__NAME_SMP_NCP}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'input'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG_OUTPUT}','{DEVICE_GATEWAY_NETWORK__NAME_OUTPUT[0]}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'output'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG_OUTPUT}','{DEVICE_GATEWAY_NETWORK__NAME_OUTPUT[1]}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'output'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    op.execute(
        f"INSERT INTO public.data_gateway_network (id, name, data_gateway_id, type_network, date_created, date_modified,user_created_id, user_modified_id, is_alive) VALUES ('{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD_LK_OUTPUT}','{DEVICE_GATEWAY_NETWORK__NAME_OUTPUT[2]}','{SERVICE_DEVICE_DB__SYS__GATEWAY_ID}','{'output'}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True)")
    # later
    # for index, data in enumerate(SERVICE_DEVICE_DB__SYS__FIRMWARE_ID):
    #     op.execute(
    #         f"INSERT INTO public.firmware (id, date_created, date_modified,user_created_id, user_modified_id, is_alive, version_name) VALUES ('{data}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True,'{SERVICE_DEVICE_DB__SYS__FIRMWARE_VERSION[index]}')")
    #     op.execute(
    #         f"INSERT INTO public.firmware_upgrade_plan (id, date_created, date_modified,user_created_id, user_modified_id, is_alive, notes, date_start, firmware_id) VALUES ('{SERVICE_DEVICE_DB__SYS__FIRMWARE_UPGRADE_PLAN_ID[index]}', '{dt_now}', '{dt_now}','{SERVICE_DEVICE_DB__SYS_USER_ID}','{SERVICE_DEVICE_DB__SYS_USER_ID}', True,'','{dt_now}','{data}')")


def downgrade():
    for id, _,in SERVICE_DEVICE_DB__SYS__MANUFACTURER:
        op.execute(f"DELETE FROM public.device_manufacturer WHERE id='{id}'")
    for id, _, _, _ in SERVICE__DEVICE_DB__SYS__DEVICE_METERING_TYPE:
        op.execute(f"DELETE FROM public.device_modification_type WHERE id='{id}'")
    for id, _, _, _, _, _ in SERVICE_DEVICE_DB__SYS__MODIFICATION_TYPE:
        op.execute(f"DELETE FROM public.device_modification_type WHERE id='{id}'")
    for id, _, _, _ in SERVICE_DEVICE_DB__SYS__MODIFICATION:
        op.execute(f"DELETE FROM public.device_modification WHERE id='{id}'")

    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_SMP_NCP}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_AGG_OUTPUT}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_LOG_OUTPUT}'")
    op.execute(f"DELETE FROM public.data_gateway_network WHERE id='{SERVICE_DEVICE_DB__SYS__GATEWAY_NETWORK_ID_OLD_LK_OUTPUT}'")
    # for index, data in enumerate(SERVICE_DEVICE_DB__SYS__FIRMWARE_ID):
    #     op.execute(
    #         f"DELETE FROM public.firmware WHERE id='{data}'")
    #     op.execute(
    #         f"DELETE FROM public.firmware_upgrade_plan WHERE id='{SERVICE_DEVICE_DB__SYS__FIRMWARE_UPGRADE_PLAN_ID[index]}'")
