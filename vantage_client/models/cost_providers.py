from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_provider import CostProvider
    from ..models.cost_providers_links import CostProvidersLinks


T = TypeVar("T", bound="CostProviders")


@_attrs_define
class CostProviders:
    """CostProviders model

    Attributes:
        links (CostProvidersLinks | Unset):
        cost_providers (list[CostProvider] | Unset):
    """

    links: CostProvidersLinks | Unset = UNSET
    cost_providers: list[CostProvider] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        cost_providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cost_providers, Unset):
            cost_providers = []
            for cost_providers_item_data in self.cost_providers:
                cost_providers_item = cost_providers_item_data.to_dict()
                cost_providers.append(cost_providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if cost_providers is not UNSET:
            field_dict["cost_providers"] = cost_providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_provider import CostProvider
        from ..models.cost_providers_links import CostProvidersLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: CostProvidersLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CostProvidersLinks.from_dict(_links)

        _cost_providers = d.pop("cost_providers", UNSET)
        cost_providers: list[CostProvider] | Unset = UNSET
        if _cost_providers is not UNSET:
            cost_providers = []
            for cost_providers_item_data in _cost_providers:
                cost_providers_item = CostProvider.from_dict(cost_providers_item_data)

                cost_providers.append(cost_providers_item)

        cost_providers = cls(
            links=links,
            cost_providers=cost_providers,
        )

        cost_providers.additional_properties = d
        return cost_providers

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
