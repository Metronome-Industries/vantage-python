from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_date_bin import DashboardDateBin
from ..models.dashboard_date_interval import DashboardDateInterval
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_widget import DashboardWidget


T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """Dashboard model

    Attributes:
        token (Union[Unset, str]):  Example: dshbrd_abcd1234567890.
        title (Union[Unset, str]): The title of the Dashboard. Example: AWS Dashboard.
        widgets (Union[Unset, list['DashboardWidget']]):
        saved_filter_tokens (Union[Unset, list[str]]): The tokens of the Saved Filters used in the Dashboard.
        date_bin (Union[Unset, DashboardDateBin]): Determines how to group costs in the Dashboard.
        date_interval (Union[Unset, DashboardDateInterval]): Determines the date range for Reports in the Dashboard.
            Guaranteed to be set to 'custom' if 'start_date' and 'end_date' are set.
        start_date (Union[Unset, str]): The start date for the date range for Reports in the Dashboard. ISO 8601
            Formatted. Overwrites 'date_interval' if set. Example: 2023-08-04.
        end_date (Union[Unset, str]): The end date for the date range for Reports in the Dashboard. ISO 8601 Formatted.
            Overwrites 'date_interval' if set. Example: 2023-09-04.
        created_at (Union[Unset, str]): The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
            Example: 2023-08-04 00:00:00+00:00.
        updated_at (Union[Unset, str]): The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
            Example: 2023-08-04 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the Dashboard is a part of. Example:
            wrkspc_abcd1234567890.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    widgets: Union[Unset, list["DashboardWidget"]] = UNSET
    saved_filter_tokens: Union[Unset, list[str]] = UNSET
    date_bin: Union[Unset, DashboardDateBin] = UNSET
    date_interval: Union[Unset, DashboardDateInterval] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        widgets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = []
            for widgets_item_data in self.widgets:
                widgets_item = widgets_item_data.to_dict()
                widgets.append(widgets_item)

        saved_filter_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        date_bin: Union[Unset, str] = UNSET
        if not isinstance(self.date_bin, Unset):
            date_bin = self.date_bin.value

        date_interval: Union[Unset, str] = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        start_date = self.start_date

        end_date = self.end_date

        created_at = self.created_at

        updated_at = self.updated_at

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if widgets is not UNSET:
            field_dict["widgets"] = widgets
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens
        if date_bin is not UNSET:
            field_dict["date_bin"] = date_bin
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dashboard_widget import DashboardWidget

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        widgets = []
        _widgets = d.pop("widgets", UNSET)
        for widgets_item_data in _widgets or []:
            widgets_item = DashboardWidget.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        _date_bin = d.pop("date_bin", UNSET)
        date_bin: Union[Unset, DashboardDateBin]
        if isinstance(_date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = DashboardDateBin(_date_bin)

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: Union[Unset, DashboardDateInterval]
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = DashboardDateInterval(_date_interval)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        dashboard = cls(
            token=token,
            title=title,
            widgets=widgets,
            saved_filter_tokens=saved_filter_tokens,
            date_bin=date_bin,
            date_interval=date_interval,
            start_date=start_date,
            end_date=end_date,
            created_at=created_at,
            updated_at=updated_at,
            workspace_token=workspace_token,
        )

        dashboard.additional_properties = d
        return dashboard

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
