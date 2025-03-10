from enum import Enum


class CreateNetworkFlowReportDateInterval(str, Enum):
    CUSTOM = "custom"
    LAST_3_DAYS = "last_3_days"
    LAST_7_DAYS = "last_7_days"

    def __str__(self) -> str:
        return str(self.value)
