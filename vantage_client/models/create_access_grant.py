from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_access_grant_access import CreateAccessGrantAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAccessGrant")


@_attrs_define
class CreateAccessGrant:
    """Create an Access Grant.

    Attributes:
        resource_token (str): The token of the resource for which you are granting access.
        team_token (str): The token of the Team you want to grant access to.
        access (Union[Unset, CreateAccessGrantAccess]): The access level you want to grant. Defaults to 'allowed'.
    """

    resource_token: str
    team_token: str
    access: Union[Unset, CreateAccessGrantAccess] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_token = self.resource_token

        team_token = self.team_token

        access: Union[Unset, str] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_token": resource_token,
                "team_token": team_token,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_token = d.pop("resource_token")

        team_token = d.pop("team_token")

        _access = d.pop("access", UNSET)
        access: Union[Unset, CreateAccessGrantAccess]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = CreateAccessGrantAccess(_access)

        create_access_grant = cls(
            resource_token=resource_token,
            team_token=team_token,
            access=access,
        )

        create_access_grant.additional_properties = d
        return create_access_grant

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
