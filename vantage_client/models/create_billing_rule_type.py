from enum import Enum


class CreateBillingRuleType(str, Enum):
    ADJUSTMENT = "adjustment"
    CHARGE = "charge"
    CREDIT = "credit"
    CUSTOM = "custom"
    EXCLUSION = "exclusion"

    def __str__(self) -> str:
        return str(self.value)
