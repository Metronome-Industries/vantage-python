from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_team_role import UpdateTeamRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTeam")


@_attrs_define
class UpdateTeam:
    """Update a Team.

    Attributes:
        name (Union[Unset, str]): The name of the Team.
        description (Union[Unset, str]): The description of the Team.
        workspace_tokens (Union[Unset, list[str]]): The Workspace tokens to associate to the Team.
        user_tokens (Union[Unset, list[str]]): The User tokens to associate to the Team.
        user_emails (Union[Unset, list[str]]): The User emails to associate to the Team.
        role (Union[Unset, UpdateTeamRole]): The role to assign to the provided Users. Defaults to 'editor' which has
            editor permissions.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    workspace_tokens: Union[Unset, list[str]] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    user_emails: Union[Unset, list[str]] = UNSET
    role: Union[Unset, UpdateTeamRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        workspace_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.workspace_tokens, Unset):
            workspace_tokens = self.workspace_tokens

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        user_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_emails, Unset):
            user_emails = self.user_emails

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if workspace_tokens is not UNSET:
            field_dict["workspace_tokens"] = workspace_tokens
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if user_emails is not UNSET:
            field_dict["user_emails"] = user_emails
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        workspace_tokens = cast(list[str], d.pop("workspace_tokens", UNSET))

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        user_emails = cast(list[str], d.pop("user_emails", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, UpdateTeamRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UpdateTeamRole(_role)

        update_team = cls(
            name=name,
            description=description,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )

        update_team.additional_properties = d
        return update_team

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
