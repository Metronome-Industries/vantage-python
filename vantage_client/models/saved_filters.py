from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.saved_filter import SavedFilter


T = TypeVar("T", bound="SavedFilters")


@_attrs_define
class SavedFilters:
    """SavedFilters model

    Attributes:
        links (Union[Unset, Links]):
        saved_filters (Union[Unset, list['SavedFilter']]):
    """

    links: Union[Unset, "Links"] = UNSET
    saved_filters: Union[Unset, list["SavedFilter"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        saved_filters: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.saved_filter import SavedFilter

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        saved_filters = []
        _saved_filters = d.pop("saved_filters", UNSET)
        for saved_filters_item_data in _saved_filters or []:
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
