from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_filter import SavedFilter
    from ..models.saved_filters_links import SavedFiltersLinks


T = TypeVar("T", bound="SavedFilters")


@_attrs_define
class SavedFilters:
    """SavedFilters model

    Attributes:
        links (SavedFiltersLinks | Unset):
        saved_filters (list[SavedFilter] | Unset):
    """

    links: SavedFiltersLinks | Unset = UNSET
    saved_filters: list[SavedFilter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        saved_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.saved_filters, Unset):
            saved_filters = []
            for saved_filters_item_data in self.saved_filters:
                saved_filters_item = saved_filters_item_data.to_dict()
                saved_filters.append(saved_filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if saved_filters is not UNSET:
            field_dict["saved_filters"] = saved_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_filter import SavedFilter
        from ..models.saved_filters_links import SavedFiltersLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: SavedFiltersLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SavedFiltersLinks.from_dict(_links)

        _saved_filters = d.pop("saved_filters", UNSET)
        saved_filters: list[SavedFilter] | Unset = UNSET
        if _saved_filters is not UNSET:
            saved_filters = []
            for saved_filters_item_data in _saved_filters:
                saved_filters_item = SavedFilter.from_dict(saved_filters_item_data)

                saved_filters.append(saved_filters_item)

        saved_filters = cls(
            links=links,
            saved_filters=saved_filters,
        )

        saved_filters.additional_properties = d
        return saved_filters

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
