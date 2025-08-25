from enum import Enum


class CreateCostExportBodySchema(str, Enum):
    FOCUS = "focus"
    VNTG = "vntg"

    def __str__(self) -> str:
        return str(self.value)
