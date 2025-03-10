from enum import Enum


class AttachedBusinessMetricForCostReportUnitScale(str, Enum):
    PER_BILLION = "per_billion"
    PER_HUNDRED = "per_hundred"
    PER_MILLION = "per_million"
    PER_THOUSAND = "per_thousand"
    PER_UNIT = "per_unit"

    def __str__(self) -> str:
        return str(self.value)
