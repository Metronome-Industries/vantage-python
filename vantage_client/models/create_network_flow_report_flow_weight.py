from enum import Enum


class CreateNetworkFlowReportFlowWeight(str, Enum):
    BYTES = "bytes"
    COSTS = "costs"

    def __str__(self) -> str:
        return str(self.value)
