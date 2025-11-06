from enum import Enum


class IntegrationStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    IMPORTED = "imported"
    IMPORTING = "importing"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
