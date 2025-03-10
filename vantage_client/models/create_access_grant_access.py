from enum import Enum


class CreateAccessGrantAccess(str, Enum):
    ALLOWED = "allowed"
    DENIED = "denied"

    def __str__(self) -> str:
        return str(self.value)
