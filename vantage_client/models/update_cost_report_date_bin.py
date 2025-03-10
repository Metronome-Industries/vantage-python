from enum import Enum


class UpdateCostReportDateBin(str, Enum):
    CUMULATIVE = "cumulative"
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
