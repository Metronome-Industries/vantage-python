from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_date_bin import UpdateDashboardDateBin
from ..models.update_dashboard_date_interval import UpdateDashboardDateInterval
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_widgets_item import UpdateDashboardWidgetsItem


T = TypeVar("T", bound="UpdateDashboard")


@_attrs_define
class UpdateDashboard:
    """Update a Dashboard.

    Attributes:
        title (str | Unset): The title of the Dashboard.
        widgets (list[UpdateDashboardWidgetsItem] | Unset): The widgets to add to the Dashboard. Currently supports
            CostReport, ResourceReport, KubernetesEfficiencyReport, and FinancialCommitmentReport.
        saved_filter_tokens (list[str] | Unset): The tokens of the Saved Filters used in the Dashboard.
        date_bin (UpdateDashboardDateBin | Unset): Determines how to group costs in the Dashboard.
        date_interval (UpdateDashboardDateInterval | Unset): Determines the date range in the Dashboard. Incompatible
            with 'start_date' and 'end_date' parameters.
        start_date (str | Unset): The start date for the date range for costs in the Dashboard. ISO 8601 Formatted.
            Incompatible with 'date_interval' parameter.
        end_date (str | Unset): The end date for the date range for costs in the Dashboard. ISO 8601 Formatted.
            Incompatible with 'date_interval' parameter.
        workspace_token (str | Unset): The token of the Workspace the Dashboard belongs to. Required if the API token is
            associated with multiple Workspaces.
    """

    title: str | Unset = UNSET
    widgets: list[UpdateDashboardWidgetsItem] | Unset = UNSET
    saved_filter_tokens: list[str] | Unset = UNSET
    date_bin: UpdateDashboardDateBin | Unset = UNSET
    date_interval: UpdateDashboardDateInterval | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    workspace_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        widgets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = []
            for widgets_item_data in self.widgets:
                widgets_item = widgets_item_data.to_dict()
                widgets.append(widgets_item)

        saved_filter_tokens: list[str] | Unset = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        date_bin: str | Unset = UNSET
        if not isinstance(self.date_bin, Unset):
            date_bin = self.date_bin.value

        date_interval: str | Unset = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        start_date = self.start_date

        end_date = self.end_date

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_dashboard_widgets_item import UpdateDashboardWidgetsItem

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _widgets = d.pop("widgets", UNSET)
        widgets: list[UpdateDashboardWidgetsItem] | Unset = UNSET
        if _widgets is not UNSET:
            widgets = []
            for widgets_item_data in _widgets:
                widgets_item = UpdateDashboardWidgetsItem.from_dict(widgets_item_data)

                widgets.append(widgets_item)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        _date_bin = d.pop("date_bin", UNSET)
        date_bin: UpdateDashboardDateBin | Unset
        if isinstance(_date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = UpdateDashboardDateBin(_date_bin)

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: UpdateDashboardDateInterval | Unset
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = UpdateDashboardDateInterval(_date_interval)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        update_dashboard = cls(
            title=title,
            widgets=widgets,
            saved_filter_tokens=saved_filter_tokens,
            date_bin=date_bin,
            date_interval=date_interval,
            start_date=start_date,
            end_date=end_date,
            workspace_token=workspace_token,
        )

        update_dashboard.additional_properties = d
        return update_dashboard

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
