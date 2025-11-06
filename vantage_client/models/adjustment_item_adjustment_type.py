from enum import Enum


class AdjustmentItemAdjustmentType(str, Enum):
    CHARGE = "charge"
    CREDIT = "credit"
    DISCOUNT = "discount"

    def __str__(self) -> str:
        return str(self.value)
