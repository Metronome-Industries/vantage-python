from enum import Enum


class UpdateNetworkFlowReportGroupingsItem(str, Enum):
    ACCOUNT_ID = "account_id"
    AZ_ID = "az_id"
    DSTADDR = "dstaddr"
    DSTHOSTNAME = "dsthostname"
    FLOW_DIRECTION = "flow_direction"
    INSTANCE_ID = "instance_id"
    INTERFACE_ID = "interface_id"
    PEER_ACCOUNT_ID = "peer_account_id"
    PEER_AZ_ID = "peer_az_id"
    PEER_INSTANCE_ID = "peer_instance_id"
    PEER_INTERFACE_ID = "peer_interface_id"
    PEER_REGION = "peer_region"
    PEER_RESOURCE_UUID = "peer_resource_uuid"
    PEER_SUBNET_ID = "peer_subnet_id"
    PEER_VPC_ID = "peer_vpc_id"
    REGION = "region"
    RESOURCE_UUID = "resource_uuid"
    SRCADDR = "srcaddr"
    SRCHOSTNAME = "srchostname"
    SUBNET_ID = "subnet_id"
    TRAFFIC_CATEGORY = "traffic_category"
    TRAFFIC_PATH = "traffic_path"
    VPC_ID = "vpc_id"

    def __str__(self) -> str:
        return str(self.value)
