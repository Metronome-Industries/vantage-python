from enum import Enum


class CreateCostReportChartType(str, Enum):
    AREA = "area"
    BAR = "bar"
    LINE = "line"
    PIE = "pie"

    def __str__(self) -> str:
        return str(self.value)
