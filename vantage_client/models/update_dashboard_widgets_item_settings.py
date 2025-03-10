from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_widgets_item_settings_display_type import UpdateDashboardWidgetsItemSettingsDisplayType

T = TypeVar("T", bound="UpdateDashboardWidgetsItemSettings")


@_attrs_define
class UpdateDashboardWidgetsItemSettings:
    """The settings for the DashboardWidget.

    Attributes:
        display_type (UpdateDashboardWidgetsItemSettingsDisplayType):
    """

    display_type: UpdateDashboardWidgetsItemSettingsDisplayType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_type = self.display_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_type": display_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_type = UpdateDashboardWidgetsItemSettingsDisplayType(d.pop("display_type"))

        update_dashboard_widgets_item_settings = cls(
            display_type=display_type,
        )

        update_dashboard_widgets_item_settings.additional_properties = d
        return update_dashboard_widgets_item_settings

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
