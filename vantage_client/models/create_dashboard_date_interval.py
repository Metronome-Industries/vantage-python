from enum import Enum


class CreateDashboardDateInterval(str, Enum):
    CUSTOM = "custom"
    LAST_12_MONTHS = "last_12_months"
    LAST_24_MONTHS = "last_24_months"
    LAST_30_DAYS = "last_30_days"
    LAST_36_MONTHS = "last_36_months"
    LAST_3_DAYS = "last_3_days"
    LAST_3_MONTHS = "last_3_months"
    LAST_6_MONTHS = "last_6_months"
    LAST_7_DAYS = "last_7_days"
    LAST_MONTH = "last_month"
    NEXT_12_MONTHS = "next_12_months"
    NEXT_3_MONTHS = "next_3_months"
    NEXT_6_MONTHS = "next_6_months"
    NEXT_MONTH = "next_month"
    THIS_MONTH = "this_month"
    YEAR_TO_DATE = "year_to_date"

    def __str__(self) -> str:
        return str(self.value)
