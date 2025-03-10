from enum import Enum


class UpdateNetworkFlowReportFlowDirection(str, Enum):
    EGRESS = "egress"
    INGRESS = "ingress"

    def __str__(self) -> str:
        return str(self.value)
