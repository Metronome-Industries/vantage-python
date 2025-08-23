from enum import Enum


class CreateCostReportChartType(str, Enum):
    AREA = "area"
    BAR = "bar"
    LINE = "line"
    MULTI_BAR = "multi_bar"
    PIE = "pie"

    def __str__(self) -> str:
        return str(self.value)
