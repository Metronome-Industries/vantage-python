from enum import Enum


class UpdateDashboardWidgetsItemSettingsDisplayType(str, Enum):
    CHART = "chart"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
