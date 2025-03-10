from enum import Enum


class UpdateTeamRole(str, Enum):
    EDITOR = "editor"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
