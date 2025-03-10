from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration import Integration
    from ..models.links import Links


T = TypeVar("T", bound="Integrations")


@_attrs_define
class Integrations:
    """Integrations model

    Attributes:
        links (Union[Unset, Links]):
        integrations (Union[Unset, list['Integration']]):
    """

    links: Union[Unset, "Links"] = UNSET
    integrations: Union[Unset, list["Integration"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        integrations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = []
            for integrations_item_data in self.integrations:
                integrations_item = integrations_item_data.to_dict()
                integrations.append(integrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if integrations is not UNSET:
            field_dict["integrations"] = integrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.integration import Integration
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        integrations = []
        _integrations = d.pop("integrations", UNSET)
        for integrations_item_data in _integrations or []:
            integrations_item = Integration.from_dict(integrations_item_data)

            integrations.append(integrations_item)

        integrations = cls(
            links=links,
            integrations=integrations,
        )

        integrations.additional_properties = d
        return integrations

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
