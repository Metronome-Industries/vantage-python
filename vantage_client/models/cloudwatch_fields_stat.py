from enum import Enum


class CloudwatchFieldsStat(str, Enum):
    AVERAGE = "Average"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    SUM = "Sum"

    def __str__(self) -> str:
        return str(self.value)
