from enum import Enum


class GetCostsDateBin(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
