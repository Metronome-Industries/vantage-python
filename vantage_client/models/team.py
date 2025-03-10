from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """Team model

    Attributes:
        token (Union[Unset, str]):
        name (Union[Unset, str]): The name of the Team. Example: Cost Savers.
        description (Union[Unset, str]): The description of the Team. Example: The Team that saves costs.
        workspace_tokens (Union[Unset, list[str]]): The tokens for any Workspaces that the Team belongs to
        user_emails (Union[Unset, list[str]]): The email addresses for Users that belong to the Team
        user_tokens (Union[Unset, list[str]]): The tokens for Users that belong to the Team
    """

    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    workspace_tokens: Union[Unset, list[str]] = UNSET
    user_emails: Union[Unset, list[str]] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        description = self.description

        workspace_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.workspace_tokens, Unset):
            workspace_tokens = self.workspace_tokens

        user_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_emails, Unset):
            user_emails = self.user_emails

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if workspace_tokens is not UNSET:
            field_dict["workspace_tokens"] = workspace_tokens
        if user_emails is not UNSET:
            field_dict["user_emails"] = user_emails
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        workspace_tokens = cast(list[str], d.pop("workspace_tokens", UNSET))

        user_emails = cast(list[str], d.pop("user_emails", UNSET))

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        team = cls(
            token=token,
            name=name,
            description=description,
            workspace_tokens=workspace_tokens,
            user_emails=user_emails,
            user_tokens=user_tokens,
        )

        team.additional_properties = d
        return team

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
