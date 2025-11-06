from enum import Enum


class UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType(str, Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
