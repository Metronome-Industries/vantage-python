from enum import Enum


class BusinessMetricImportType(str, Enum):
    CLOUDWATCH = "cloudwatch"
    CSV = "csv"
    DATADOG_METRICS = "datadog_metrics"

    def __str__(self) -> str:
        return str(self.value)
