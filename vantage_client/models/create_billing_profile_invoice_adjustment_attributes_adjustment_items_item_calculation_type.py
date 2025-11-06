from enum import Enum


class CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType(str, Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
