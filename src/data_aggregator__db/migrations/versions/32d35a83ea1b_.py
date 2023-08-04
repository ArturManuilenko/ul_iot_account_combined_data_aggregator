"""empty message

Revision ID: 19a1ad377be0
Revises: 610c0fe71413
Create Date: 2021-11-02 12:25:04.056594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32d35a83ea1b'
down_revision = '610c0fe71413'
branch_labels = None
depends_on = None


DEVICE_GATEWAY_NETWORK__BS0_OLD_ID = '324570cc-aef6-4a05-8989-ee246155bf7d'
DEVICE_GATEWAY_NETWORK__BS0_NEW_NAME = 'BS0'
DEVICE_GATEWAY_NETWORK__BS0_OLD_ID_DUPLICATE = '98c028d6-f71b-407b-ad70-02e805e6fb86'
DEVICE_GATEWAY_NETWORK__SMP_OLD_ID_DUPLICATE  = '3b0ab436-7357-4041-8533-0b48b41d097d'
DEVICE_GATEWAY_NETWORK__NCP_SMP_OLD_ID_DUPLICATE  = 'c11e99b9-eaaa-4972-a34f-2303da768ac8'
DEVICE_GATEWAY_NETWORK__AGREGATOR_OLD_ID_DUPLICATE  = 'a5981f6b-98cd-4899-8d6d-174a5c5b0b6f'
DEVICE_GATEWAY_NETWORK__LOGGER_OLD_ID_DUPLICATE  = 'be1b3408-13c2-43c3-b151-213a662d2fcf'


def upgrade():
    op.execute("UPDATE data_gateway_network "
                f"SET name = '{DEVICE_GATEWAY_NETWORK__BS0_NEW_NAME}' "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__BS0_OLD_ID}';")
    op.execute("DELETE FROM data_gateway_network_device "
                f"WHERE data_gateway_network_id = '{DEVICE_GATEWAY_NETWORK__BS0_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network_device "
                f"WHERE data_gateway_network_id = '{DEVICE_GATEWAY_NETWORK__SMP_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network_device "
                f"WHERE data_gateway_network_id = '{DEVICE_GATEWAY_NETWORK__NCP_SMP_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network_device "
                f"WHERE data_gateway_network_id = '{DEVICE_GATEWAY_NETWORK__AGREGATOR_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network_device "
                f"WHERE data_gateway_network_id = '{DEVICE_GATEWAY_NETWORK__LOGGER_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__BS0_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__SMP_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__NCP_SMP_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__AGREGATOR_OLD_ID_DUPLICATE}';")
    op.execute("DELETE FROM data_gateway_network "
                f"WHERE id = '{DEVICE_GATEWAY_NETWORK__LOGGER_OLD_ID_DUPLICATE}';")


def downgrade():
    pass