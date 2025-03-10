from enum import Enum


class CreateKubernetesEfficiencyReportDateBucket(str, Enum):
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
