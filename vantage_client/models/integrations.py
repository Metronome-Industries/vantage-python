from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration import Integration
    from ..models.integrations_links import IntegrationsLinks


T = TypeVar("T", bound="Integrations")


@_attrs_define
class Integrations:
    """Integrations model

    Attributes:
        links (IntegrationsLinks | Unset):
        integrations (list[Integration] | Unset):
    """

    links: IntegrationsLinks | Unset = UNSET
    integrations: list[Integration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        integrations: list[dict[str, Any]] | Unset = UNSET
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration import Integration
        from ..models.integrations_links import IntegrationsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: IntegrationsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IntegrationsLinks.from_dict(_links)

        _integrations = d.pop("integrations", UNSET)
        integrations: list[Integration] | Unset = UNSET
        if _integrations is not UNSET:
            integrations = []
            for integrations_item_data in _integrations:
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
