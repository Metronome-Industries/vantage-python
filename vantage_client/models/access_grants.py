from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_grant import AccessGrant
    from ..models.links import Links


T = TypeVar("T", bound="AccessGrants")


@_attrs_define
class AccessGrants:
    """AccessGrants model

    Attributes:
        links (Union[Unset, Links]):
        access_grants (Union[Unset, list['AccessGrant']]):
    """

    links: Union[Unset, "Links"] = UNSET
    access_grants: Union[Unset, list["AccessGrant"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        access_grants: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access_grant import AccessGrant
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        access_grants = []
        _access_grants = d.pop("access_grants", UNSET)
        for access_grants_item_data in _access_grants or []:
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
