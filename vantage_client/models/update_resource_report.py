from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateResourceReport")


@_attrs_define
class UpdateResourceReport:
    """Update a ResourceReport.

    Attributes:
        title (Union[Unset, str]): The title of the ResourceReport.
        filter_ (Union[Unset, str]): The filter query language to apply to the ResourceReport. Additional documentation
            available at https://docs.vantage.sh/vql.
        columns (Union[Unset, list[str]]): Array of column names to display in the table. Column names should match
            those returned by the /resource_reports/columns endpoint. The order determines the display order. Only available
            for reports with a single resource type filter.
    """

    title: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    columns: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        filter_ = self.filter_

        columns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        filter_ = d.pop("filter", UNSET)

        columns = cast(list[str], d.pop("columns", UNSET))

        update_resource_report = cls(
            title=title,
            filter_=filter_,
            columns=columns,
        )

        update_resource_report.additional_properties = d
        return update_resource_report

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
