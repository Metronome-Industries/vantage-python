from enum import Enum


class CreateFinancialCommitmentReportOnDemandCostsScope(str, Enum):
    ALL = "all"
    DISCOUNTABLE = "discountable"

    def __str__(self) -> str:
        return str(self.value)
