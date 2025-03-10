from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_widgets_item_settings import UpdateDashboardWidgetsItemSettings


T = TypeVar("T", bound="UpdateDashboardWidgetsItem")


@_attrs_define
class UpdateDashboardWidgetsItem:
    """
    Attributes:
        widgetable_token (str): The token of the represented Resource.
        title (Union[Unset, str]): The title of the Widget (defaults to the title of the Resource).
        settings (Union[Unset, UpdateDashboardWidgetsItemSettings]): The settings for the DashboardWidget.
    """

    widgetable_token: str
    title: Union[Unset, str] = UNSET
    settings: Union[Unset, "UpdateDashboardWidgetsItemSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        widgetable_token = self.widgetable_token

        title = self.title

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "widgetable_token": widgetable_token,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_dashboard_widgets_item_settings import UpdateDashboardWidgetsItemSettings

        d = src_dict.copy()
        widgetable_token = d.pop("widgetable_token")

        title = d.pop("title", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, UpdateDashboardWidgetsItemSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = UpdateDashboardWidgetsItemSettings.from_dict(_settings)

        update_dashboard_widgets_item = cls(
            widgetable_token=widgetable_token,
            title=title,
            settings=settings,
        )

        update_dashboard_widgets_item.additional_properties = d
        return update_dashboard_widgets_item

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
