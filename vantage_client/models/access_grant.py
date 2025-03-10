from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessGrant")


@_attrs_define
class AccessGrant:
    """AccessGrant model

    Attributes:
        token (Union[Unset, str]):
        resource_token (Union[Unset, str]): The token for any resource the AccessGrant is applied to. Example:
            rprt_abcd1234.
        access (Union[Unset, str]): The access status of the AccessGrant.
        team_token (Union[Unset, str]): The Team token for which an AccessGrant is applied to.
        created_at (Union[Unset, str]): The date and time, in UTC, the AccessGrant was created. ISO 8601 Formatted.
            Example: 2023-08-04 00:00:00+00:00.
        created_by (Union[Unset, str]): The token for the User who created the AccessGrant.
    """

    token: Union[Unset, str] = UNSET
    resource_token: Union[Unset, str] = UNSET
    access: Union[Unset, str] = UNSET
    team_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        resource_token = self.resource_token

        access = self.access

        team_token = self.team_token

        created_at = self.created_at

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if resource_token is not UNSET:
            field_dict["resource_token"] = resource_token
        if access is not UNSET:
            field_dict["access"] = access
        if team_token is not UNSET:
            field_dict["team_token"] = team_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        resource_token = d.pop("resource_token", UNSET)

        access = d.pop("access", UNSET)

        team_token = d.pop("team_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by = d.pop("created_by", UNSET)

        access_grant = cls(
            token=token,
            resource_token=resource_token,
            access=access,
            team_token=team_token,
            created_at=created_at,
            created_by=created_by,
        )

        access_grant.additional_properties = d
        return access_grant

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
