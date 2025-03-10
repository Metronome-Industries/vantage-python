from enum import Enum


class UpdateWorkspaceFilesBodyExchangeRateDate(str, Enum):
    DAILY_RATE = "daily_rate"
    END_OF_BILLING_PERIOD_RATE = "end_of_billing_period_rate"

    def __str__(self) -> str:
        return str(self.value)
