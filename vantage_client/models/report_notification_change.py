from enum import Enum


class ReportNotificationChange(str, Enum):
    DOLLARS = "dollars"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
