from enum import Enum


class CreateDashboardWidgetsItemSettingsDisplayType(str, Enum):
    CHART = "chart"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
