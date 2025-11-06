from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_widget_settings_display_type import DashboardWidgetSettingsDisplayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardWidgetSettings")


@_attrs_define
class DashboardWidgetSettings:
    """
    Attributes:
        display_type (DashboardWidgetSettingsDisplayType | Unset):
    """

    display_type: DashboardWidgetSettingsDisplayType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_type: str | Unset = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_type is not UNSET:
            field_dict["display_type"] = display_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _display_type = d.pop("display_type", UNSET)
        display_type: DashboardWidgetSettingsDisplayType | Unset
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = DashboardWidgetSettingsDisplayType(_display_type)

        dashboard_widget_settings = cls(
            display_type=display_type,
        )

        dashboard_widget_settings.additional_properties = d
        return dashboard_widget_settings

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
