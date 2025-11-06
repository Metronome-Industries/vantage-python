from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCostReportChartSettings")


@_attrs_define
class UpdateCostReportChartSettings:
    """Report chart settings.

    Attributes:
        x_axis_dimension (list[str] | Unset): The dimension used to group or label data along the x-axis (e.g., by date,
            region, or service). NOTE: Only one value is allowed at this time. Defaults to ['date'].
        y_axis_dimension (str | Unset): The metric or measure displayed on the chart’s y-axis. Possible values: 'cost',
            'usage'. Defaults to 'cost'.
    """

    x_axis_dimension: list[str] | Unset = UNSET
    y_axis_dimension: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x_axis_dimension: list[str] | Unset = UNSET
        if not isinstance(self.x_axis_dimension, Unset):
            x_axis_dimension = self.x_axis_dimension

        y_axis_dimension = self.y_axis_dimension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x_axis_dimension is not UNSET:
            field_dict["x_axis_dimension"] = x_axis_dimension
        if y_axis_dimension is not UNSET:
            field_dict["y_axis_dimension"] = y_axis_dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_axis_dimension = cast(list[str], d.pop("x_axis_dimension", UNSET))

        y_axis_dimension = d.pop("y_axis_dimension", UNSET)

        update_cost_report_chart_settings = cls(
            x_axis_dimension=x_axis_dimension,
            y_axis_dimension=y_axis_dimension,
        )

        update_cost_report_chart_settings.additional_properties = d
        return update_cost_report_chart_settings

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
