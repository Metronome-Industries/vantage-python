from enum import Enum


class DashboardWidgetSettingsDisplayType(str, Enum):
    CHART = "chart"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
