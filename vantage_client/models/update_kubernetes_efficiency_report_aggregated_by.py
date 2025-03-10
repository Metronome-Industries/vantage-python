from enum import Enum


class UpdateKubernetesEfficiencyReportAggregatedBy(str, Enum):
    AMOUNT = "amount"
    COST_EFFICIENCY = "cost_efficiency"
    IDLE_COST = "idle_cost"

    def __str__(self) -> str:
        return str(self.value)
