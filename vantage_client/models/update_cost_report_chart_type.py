from enum import Enum


class UpdateCostReportChartType(str, Enum):
    AREA = "area"
    BAR = "bar"
    LINE = "line"
    PIE = "pie"

    def __str__(self) -> str:
        return str(self.value)
