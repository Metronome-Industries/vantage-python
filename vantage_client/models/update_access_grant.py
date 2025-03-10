from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_access_grant_access import UpdateAccessGrantAccess

T = TypeVar("T", bound="UpdateAccessGrant")


@_attrs_define
class UpdateAccessGrant:
    """Update an AccessGrant.

    Attributes:
        access (UpdateAccessGrantAccess): Allowed or denied access to resource.
    """

    access: UpdateAccessGrantAccess
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access = UpdateAccessGrantAccess(d.pop("access"))

        update_access_grant = cls(
            access=access,
        )

        update_access_grant.additional_properties = d
        return update_access_grant

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
