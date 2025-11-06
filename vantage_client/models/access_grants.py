from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_grant import AccessGrant
    from ..models.access_grants_links import AccessGrantsLinks


T = TypeVar("T", bound="AccessGrants")


@_attrs_define
class AccessGrants:
    """AccessGrants model

    Attributes:
        links (AccessGrantsLinks | Unset):
        access_grants (list[AccessGrant] | Unset):
    """

    links: AccessGrantsLinks | Unset = UNSET
    access_grants: list[AccessGrant] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        access_grants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_grants, Unset):
            access_grants = []
            for access_grants_item_data in self.access_grants:
                access_grants_item = access_grants_item_data.to_dict()
                access_grants.append(access_grants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if access_grants is not UNSET:
            field_dict["access_grants"] = access_grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_grant import AccessGrant
        from ..models.access_grants_links import AccessGrantsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: AccessGrantsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AccessGrantsLinks.from_dict(_links)

        _access_grants = d.pop("access_grants", UNSET)
        access_grants: list[AccessGrant] | Unset = UNSET
        if _access_grants is not UNSET:
            access_grants = []
            for access_grants_item_data in _access_grants:
                access_grants_item = AccessGrant.from_dict(access_grants_item_data)

                access_grants.append(access_grants_item)

        access_grants = cls(
            links=links,
            access_grants=access_grants,
        )

        access_grants.additional_properties = d
        return access_grants

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
