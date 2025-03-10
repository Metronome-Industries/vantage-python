from enum import Enum


class UpdateFinancialCommitmentReportDateBucket(str, Enum):
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
