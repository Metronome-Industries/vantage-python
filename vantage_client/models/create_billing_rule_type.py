from enum import Enum


class CreateBillingRuleType(str, Enum):
    ADJUSTMENT = "adjustment"
    CHARGE = "charge"
    CREDIT = "credit"
    EXCLUSION = "exclusion"

    def __str__(self) -> str:
        return str(self.value)
