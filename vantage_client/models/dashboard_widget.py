from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_widget_settings import DashboardWidgetSettings


T = TypeVar("T", bound="DashboardWidget")


@_attrs_define
class DashboardWidget:
    """
    Attributes:
        widgetable_token (str | Unset):  Example: rprt_a12b3c.
        title (str | Unset): The title of the Widget. Example: My Widget.
        settings (DashboardWidgetSettings | Unset):
    """

    widgetable_token: str | Unset = UNSET
    title: str | Unset = UNSET
    settings: DashboardWidgetSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        widgetable_token = self.widgetable_token

        title = self.title

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if widgetable_token is not UNSET:
            field_dict["widgetable_token"] = widgetable_token
        if title is not UNSET:
            field_dict["title"] = title
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_widget_settings import DashboardWidgetSettings

        d = dict(src_dict)
        widgetable_token = d.pop("widgetable_token", UNSET)

        title = d.pop("title", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: DashboardWidgetSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = DashboardWidgetSettings.from_dict(_settings)

        dashboard_widget = cls(
            widgetable_token=widgetable_token,
            title=title,
            settings=settings,
        )

        dashboard_widget.additional_properties = d
        return dashboard_widget

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
