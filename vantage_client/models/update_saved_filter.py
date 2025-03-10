from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSavedFilter")


@_attrs_define
class UpdateSavedFilter:
    """Update a SavedFilter for CostReports.

    Attributes:
        title (Union[Unset, str]): The title of the SavedFilter.
        filter_ (Union[Unset, str]): The filter query language to apply to the SavedFilter, which subsequently gets
            applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    """

    title: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        filter_ = d.pop("filter", UNSET)

        update_saved_filter = cls(
            title=title,
            filter_=filter_,
        )

        update_saved_filter.additional_properties = d
        return update_saved_filter

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
