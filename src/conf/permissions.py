from api_utils.access import PermissionRegistry


permissions_registry = PermissionRegistry('ul_iot_account_DA_service', 11000, 12000)

# DataGateway API methods
PERMISSION__DA_GET_DATA_GATEWAYS_LIST = permissions_registry.add('DA_GET_DATA_GATEWAYS_LIST', 1, 'get data gateways list', 'data gateway')
PERMISSION__DA_GET_DATA_GATEWAY = permissions_registry.add('DA_GET_DATA_GATEWAY', 2, 'get data gateway', 'data gateway')
PERMISSION__DA_MK_DATA_GATEWAY = permissions_registry.add('DA_MK_DATA_GATEWAY', 3, 'create data gateway', 'data gateway')
PERMISSION__DA_DEL_DATA_GATEWAY = permissions_registry.add('DA_DEL_DATA_GATEWAY', 4, 'delete data gateway', 'data gateway')
PERMISSION__DA_MOD_DATA_GATEWAY = permissions_registry.add('DA_MOD_DATA_GATEWAY', 5, 'update data gateway', 'data gateway')

# DataGatewayNetwork API methods
PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_LIST = permissions_registry.add('DA_GET_DATA_GATEWAY_NETWORKS_LIST', 6, 'get data gateway networks list', 'data gateway network')  # noqa: E501
PERMISSION__DA_GET_DATA_GATEWAY_NETWORK = permissions_registry.add('DA_GET_DATA_GATEWAY_NETWORK', 7, 'get data gateway network', 'data gateway network')
PERMISSION__DA_MK_DATA_GATEWAY_NETWORK = permissions_registry.add('DA_MK_DATA_GATEWAY_NETWORK', 8, 'create data gateway network', 'data gateway network')
PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_LIST_ALL = permissions_registry.add('DA_GET_DATA_GATEWAY_NETWORKS_LIST_ALL', 9, 'get data gateway network list all', 'data gateway network')  # noqa: E501
PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_BY_ID = permissions_registry.add('DA_GET_DATA_GATEWAY_NETWORKS_BY_ID', 10, 'get data gateway networks by id', 'data gateway network')  # noqa: E501
PERMISSION__DA_DEL_DATA_GATEWAY_NETWORK = permissions_registry.add('DA_DEL_DATA_GATEWAY_NETWORK', 39, 'delete gateway network', 'data gateway network')
PERMISSION__DA_GET_DATA_GATEWAY_NETWORK_DEVICES_LIST = permissions_registry.add(
    'DA_GET_DATA_GATEWAY_NETWORK_DEVICES_LIST',
    41, 'get data gateway network',
    'data gateway network device'
)


# DataGatewayNetworkDevice API methods
PERMISSION__DA_ADD_DEVICE_TO_DATA_GATEWAY_NETWORK = permissions_registry.add('DA_ADD_DEVICE_TO_DATA_GATEWAY_NETWORK', 11, 'update data gateway device', 'data gateway device')  # noqa: E501
PERMISSION__DA_DEL_DEVICE_FROM_DATA_GATEWAY_NETWORK = permissions_registry.add('DA_DEL_DEVICE_FROM_DATA_GATEWAY_NETWORK', 12, 'delete data gateway device', 'data gateway device')  # noqa: E501
PERMISSION__DA_GET_DATA_GATEWAY_DEVICE = permissions_registry.add('DA_GET_DATA_GATEWAY_DEVICE', 13, 'get data gateway device', 'data gateway device')

# Device API methods
PERMISSION__DA_GET_DEVICE = permissions_registry.add('DA_GET_DEVICE', 14, 'get device', 'device')
PERMISSION__DA_GET_DEVICES_LIST = permissions_registry.add('DA_GET_DEVICES_LIST', 15, 'get devices list', 'device')
PERMISSION__DA_GET_DEVICE_FACTORY_PARAMETERS = permissions_registry.add('DA_GET_DEVICE_FACTORY_PARAMETERS', 16, 'get device_factory_parameters', 'device')
PERMISSION__DA_MK_DEVICE = permissions_registry.add('DA_MK_DEVICE', 17, 'create device', 'device')
PERMISSION__DA_MOD_DEVICE = permissions_registry.add('DA_MOD_DEVICE', 18, 'update device', 'device')


# DeviceType API methods
PERMISSION__DA_GET_DEVICE_TYPES_LIST = permissions_registry.add('DA_GET_DEVICE_TYPES_LIST', 19, 'get device types list', 'device type')
PERMISSION__DA_GET_DEVICE_TYPE = permissions_registry.add('DA_GET_DEVICE_TYPE', 20, 'get device type', 'device type')
PERMISSION__DA_MK_DEVICE_TYPE = permissions_registry.add('DA_MK_DEVICE_TYPE', 21, 'create device type', 'device type')
PERMISSION__DA_DEL_DEVICE_TYPE = permissions_registry.add('DA_DEL_DEVICE_TYPE', 22, 'delete device type', 'device type')
PERMISSION__DA_MOD_DEVICE_TYPE = permissions_registry.add('DA_MOD_DEVICE_TYPE', 23, 'update device type', 'device type')

# Protocol API methods
PERMISSION__DA_GET_PROTOCOLS_LIST = permissions_registry.add('DA_GET_PROTOCOLS_LIST', 24, 'get protocols list', 'protocol')
PERMISSION__DA_GET_PROTOCOL = permissions_registry.add('DA_GET_PROTOCOL', 25, 'get protocol', 'protocol')
PERMISSION__DA_MK_PROTOCOL = permissions_registry.add('DA_MK_PROTOCOL', 26, 'create protocol', 'protocol')
PERMISSION__DA_DEL_PROTOCOL = permissions_registry.add('DA_DEL_PROTOCOL', 27, 'delete protocol', 'protocol')
PERMISSION__DA_MOD_PROTOCOL = permissions_registry.add('DA_MOD_PROTOCOL', 28, 'update protocol', 'protocol')

# DeviceManufacturer API methods
PERMISSION__DA_GET_MANUFACTURERS_LIST = permissions_registry.add('DA_GET_MANUFACTURERS_LIST', 29, 'get device manufacturers list', 'device manufacturer')
PERMISSION__DA_GET_MANUFACTURER = permissions_registry.add('DA_GET_MANUFACTURER', 30, 'get device manufacturer', 'device manufacturer')
PERMISSION__DA_MK_MANUFACTURER = permissions_registry.add('DA_MK_MANUFACTURER', 31, 'create device manufacturer', 'device manufacturer')
PERMISSION__DA_DEL_MANUFACTURER = permissions_registry.add('DA_DEL_MANUFACTURER', 32, 'delete device manufacturer', 'device manufacturer')
PERMISSION__DA_MOD_MANUFACTURER = permissions_registry.add('DA_MOD_MANUFACTURER', 33, 'update device manufacturer', 'device manufacturer')

# DeviceModification API methods
PERMISSION__DA_GET_DEVICE_MODIFICATION = permissions_registry.add('DA_GET_DEVICE_MODIFICATION', 34, 'get device modification', 'device modification')
PERMISSION__DA_GET_DEVICE_MODIFICATIONS_LIST = permissions_registry.add('DA_GET_DEVICE_MODIFICATIONS_LIST', 35, 'get device modifications list', 'device modification')  # noqa: E501
PERMISSION__DA_MK_DEVICE_MODIFICATION = permissions_registry.add('DA_MK_DEVICE_MODIFICATION', 36, 'create device modification', 'device modification')
PERMISSION__DA_MOD_DEVICE_MODIFICATION = permissions_registry.add('DA_MOD_DEVICE_MODIFICATION', 37, 'update device modification', 'device modification')
PERMISSION__DA_DEL_DEVICE_MODIFICATION = permissions_registry.add('DA_DEL_DEVICE_MODIFICATION', 38, 'delete device modification', 'device modification')

# Firmware API methods
# PERMISSION__DA_GET_FIRMWARE = permissions_registry.add('DA_GET_FIRMWARE', 39, 'get firmware', 'firmware')
# PERMISSION__DA_GET_FIRMWARES_LIST = permissions_registry.add('DA_GET_FIRMWARES_LIST', 40, 'get firmwares list', 'firmware')
# PERMISSION__DA_MK_FIRMWARE = permissions_registry.add('DA_MK_FIRMWARE', 41, 'create firmware', 'firmware')

# # HardwareVersion API methods
# PERMISSION__DA_GET_HARDWARE_VERSION = permissions_registry.add('DA_GET_HARDWARE_VERSION', 42, 'get hardware version', 'hardware version')
# PERMISSION__DA_GET_HARDWARE_VERSIONS_LIST = permissions_registry.add('DA_GET_HARDWARE_VERSIONS_LIST', 43, 'get hardware versions list', 'hardware version')
# PERMISSION__DA_MK_HARDWARE_VERSION = permissions_registry.add('DA_MK_HARDWARE_VERSION', 44, 'create hardware version', 'hardware version')
# PERMISSION__DA_MOD_HARDWARE_VERSION = permissions_registry.add('DA_MOD_HARDWARE_VERSION', 45, 'update hardware version', 'hardware version')
# PERMISSION__DA_DEL_HARDWARE_VERSION = permissions_registry.add('DA_DEL_HARDWARE_VERSION', 46, 'delete hardware version', 'hardware version')

# DeviceMeteringType API methods
PERMISSION__DA_GET_DEVICE_METERING_TYPE = permissions_registry.add('DA_GET_DEVICE_METERING_TYPE', 42, 'get device metering type', 'device metering type')
PERMISSION__DA_GET_DEVICE_METERING_TYPE_LIST = permissions_registry.add('DA_GET_DEVICE_METERING_TYPES_LIST', 43, 'get device metering type list', 'device metering type')  # noqa: E501
PERMISSION__DA_MK_DEVICE_METERING_TYPE = permissions_registry.add('DA_MK_DEVICE_METERING_TYPE', 44, 'create device metering type', 'device metering type')
PERMISSION__DA_DEL_DEVICE_METERING_TYPE = permissions_registry.add('DA_DEL_DEVICE_METERING_TYPE', 45, 'deleted device metering type', 'device metering type')

# # Mark API methods
# PERMISSION__DA_GET_MARK = permissions_registry.add('DA_GET_MARK', 47, 'get mark', 'mark')
# PERMISSION__DA_GET_MARKS_LIST = permissions_registry.add('DA_GET_MARKS_LIST', 48, 'get marks list', 'mark')
# PERMISSION__DA_MK_MARK = permissions_registry.add('DA_MK_MARK', 49, 'create mark', 'mark')
# PERMISSION__DA_MOD_MARK = permissions_registry.add('DA_MOD_MARK', 50, 'update mark', 'mark')
# PERMISSION__DA_DEL_MARK = permissions_registry.add('DA_DEL_MARK', 51, 'delete mark', 'mark')

# DeviceModificationType API methods
PERMISSION__DA_GET_DEVICE_MODIFICATION_TYPE = permissions_registry\
    .add('DA_GET_DEVICE_MODIFICATION_TYPE', 47, 'get device modification type', 'device modification type')
PERMISSION__DA_GET_DEVICE_MODIFICATIONS_TYPE_LIST = permissions_registry\
    .add('DA_GET_DEVICE_MODIFICATIONS_TYPE_LIST', 48, 'get device modification type list', 'device modification type')
PERMISSION__DA_GET_DEVICE_MODIFICATION_TYPE_BY_METERING_TYPE_ID = permissions_registry\
    .add('DA_GET_DEVICE_MODIFICATION_TYPE_BY_METERING_TYPE_ID', 49, 'get device modification type by metering type id', 'device modification type')  # noqa: E501
PERMISSION__DA_MK_DEVICE_MODIFICATION_TYPE = permissions_registry.add('DA_MK_DEVICE_MODIFICATION_TYPE', 50, 'create modification type', 'device modification type')
PERMISSION__DA_DEL_DEVICE_MODIFICATION_TYPE = permissions_registry.add('DA_DEL_DEVICE_MODIFICATION_TYPE', 51, 'delete modification type', 'device modification type')


# NEW PERMISSIONS

# Device API methods
PERMISSION__DA_MOD_DEVICE__DEVICE_MODIFICATION = permissions_registry.add('DA_MOD_DEVICE__DEVICE_MODIFICATION', 52, 'update device device modification', 'device')
PERMISSION__DA_GET_DEVICE_MODIFICATION_BY_MODIFICATION_TYPE_ID = permissions_registry\
    .add('DA_GET_DEVICE_MODIFICATION_BY_MODIFICATION_TYPE_ID', 46, 'get device modification by modification type id', 'device modification')  # noqa: E501

PERMISSION__DA_MOD_DEVICE_MANUFACTURER_SERIAL_NUMBER = permissions_registry\
    .add('DA_MOD_DEVICE_MANUFACTURER_SERIAL_NUMBER', 53, 'update device manufacturer serial_number', 'device')
PERMISSION__DA_MOD_DEVICE__FACTORY_PARAMETERS = permissions_registry.add('DA_MOD_DEVICE__FACTORY_PARAMETERS', 40, 'update device factory parameters', 'device')


PERMISSION__DA_GET_DEVICE_EVENTS = permissions_registry.add('DA_GET_DEVICE_EVENTS', 54, 'get event list', 'event')
PERMISSION__DA_GET_DEVICE_EVENTS_INTERPRETATION = permissions_registry.add('DA_GET_DEVICE_EVENTS_INTERPRETATION', 55, 'get event list  interpretation', 'event')
PERMISSION__DA_GET_DEVICE_TEMPERATURE = permissions_registry.add('DA_GET_DEVICE_TEMPERATURE', 56, 'get temperature list', 'temperature')
PERMISSION__DA_GET_DEVICE_TEMPERATURE_INTERPRETATION = permissions_registry\
    .add('DA_GET_DEVICE_TEMPERATURE_INTERPRETATION', 57, 'get temperature list interpretation', 'temperature')
PERMISSION__DA_GET_DEVICE_BATTERY = permissions_registry.add('DA_GET_DEVICE_BATTERY', 58, 'get battery list', 'battery')
DA_GET_DEVICE_BATTERY_INTERPRETATION = permissions_registry.add('DA_GET_DEVICE_BATTERY_INTERPRETATION', 59, 'get battery list interpretation', 'battery')
DA_GET_DEVICE_VALUE = permissions_registry.add('DA_GET_DEVICE_VALUE', 60, 'get value list', 'value')
DA_GET_DEVICE_VALUE_INTERPRETATION = permissions_registry.add('DA_GET_DEVICE_VALUE_INTERPRETATION', 61, 'get value list interpretation', 'value')
