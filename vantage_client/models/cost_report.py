from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_business_metric_for_cost_report import AttachedBusinessMetricForCostReport
    from ..models.chart_settings import ChartSettings
    from ..models.cost_report_settings import CostReportSettings


T = TypeVar("T", bound="CostReport")


@_attrs_define
class CostReport:
    """CostReport model

    Attributes:
        token (str | Unset):
        title (str | Unset): The title of the CostReport. Example: Production Environment.
        folder_token (str | Unset): The token for the Folder the CostReport is a part of.
        saved_filter_tokens (list[str] | Unset): The tokens for the SavedFilters assigned to the CostReport.
        business_metric_tokens_with_metadata (list[AttachedBusinessMetricForCostReport] | Unset): The tokens for the
            BusinessMetrics assigned to the CostReport, the unit scale, and label filter.
        filter_ (str | Unset): The filter applied to the CostReport. Additional documentation available at
            https://docs.vantage.sh/vql.
        groupings (str | Unset): The grouping aggregations applied to the filtered data. Example: provider, service.
        settings (CostReportSettings | Unset): Report settings.
        created_at (str | Unset): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2021-07-09T00:00:00Z.
        workspace_token (str | Unset): The token for the Workspace the CostReport is a part of.
        previous_period_start_date (str | Unset): The previous period start date of the CostReport. ISO 8601 Formatted.
            Example: 2024-06-01.
        previous_period_end_date (str | Unset): The previous period end date of the CostReport. ISO 8601 Formatted.
            Example: 2024-06-15.
        start_date (str | Unset): The start date of the CostReports. ISO 8601 Formatted. Overwrites 'date_interval' if
            set. Example: 2024-07-01.
        end_date (str | Unset): The end date of the CostReports. ISO 8601 Formatted. Overwrites 'date_interval' if set.
            Example: 2024-07-15.
        date_interval (str | Unset): The date interval of the CostReport.
        chart_type (str | Unset): The chart type of the CostReport.
        date_bin (str | Unset): The date bin of the CostReport.
        chart_settings (ChartSettings | Unset):
    """

    token: str | Unset = UNSET
    title: str | Unset = UNSET
    folder_token: str | Unset = UNSET
    saved_filter_tokens: list[str] | Unset = UNSET
    business_metric_tokens_with_metadata: list[AttachedBusinessMetricForCostReport] | Unset = UNSET
    filter_: str | Unset = UNSET
    groupings: str | Unset = UNSET
    settings: CostReportSettings | Unset = UNSET
    created_at: str | Unset = UNSET
    workspace_token: str | Unset = UNSET
    previous_period_start_date: str | Unset = UNSET
    previous_period_end_date: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    date_interval: str | Unset = UNSET
    chart_type: str | Unset = UNSET
    date_bin: str | Unset = UNSET
    chart_settings: ChartSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        folder_token = self.folder_token

        saved_filter_tokens: list[str] | Unset = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        business_metric_tokens_with_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.business_metric_tokens_with_metadata, Unset):
            business_metric_tokens_with_metadata = []
            for business_metric_tokens_with_metadata_item_data in self.business_metric_tokens_with_metadata:
                business_metric_tokens_with_metadata_item = business_metric_tokens_with_metadata_item_data.to_dict()
                business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        filter_ = self.filter_

        groupings = self.groupings

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        created_at = self.created_at

        workspace_token = self.workspace_token

        previous_period_start_date = self.previous_period_start_date

        previous_period_end_date = self.previous_period_end_date

        start_date = self.start_date

        end_date = self.end_date

        date_interval = self.date_interval

        chart_type = self.chart_type

        date_bin = self.date_bin

        chart_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chart_settings, Unset):
            chart_settings = self.chart_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if folder_token is not UNSET:
            field_dict["folder_token"] = folder_token
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens
        if business_metric_tokens_with_metadata is not UNSET:
            field_dict["business_metric_tokens_with_metadata"] = business_metric_tokens_with_metadata
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if settings is not UNSET:
            field_dict["settings"] = settings
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if previous_period_start_date is not UNSET:
            field_dict["previous_period_start_date"] = previous_period_start_date
        if previous_period_end_date is not UNSET:
            field_dict["previous_period_end_date"] = previous_period_end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if chart_type is not UNSET:
            field_dict["chart_type"] = chart_type
        if date_bin is not UNSET:
            field_dict["date_bin"] = date_bin
        if chart_settings is not UNSET:
            field_dict["chart_settings"] = chart_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_business_metric_for_cost_report import AttachedBusinessMetricForCostReport
        from ..models.chart_settings import ChartSettings
        from ..models.cost_report_settings import CostReportSettings

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        folder_token = d.pop("folder_token", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        _business_metric_tokens_with_metadata = d.pop("business_metric_tokens_with_metadata", UNSET)
        business_metric_tokens_with_metadata: list[AttachedBusinessMetricForCostReport] | Unset = UNSET
        if _business_metric_tokens_with_metadata is not UNSET:
            business_metric_tokens_with_metadata = []
            for business_metric_tokens_with_metadata_item_data in _business_metric_tokens_with_metadata:
                business_metric_tokens_with_metadata_item = AttachedBusinessMetricForCostReport.from_dict(
                    business_metric_tokens_with_metadata_item_data
                )

                business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        filter_ = d.pop("filter", UNSET)

        groupings = d.pop("groupings", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: CostReportSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = CostReportSettings.from_dict(_settings)

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        previous_period_start_date = d.pop("previous_period_start_date", UNSET)

        previous_period_end_date = d.pop("previous_period_end_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        date_interval = d.pop("date_interval", UNSET)

        chart_type = d.pop("chart_type", UNSET)

        date_bin = d.pop("date_bin", UNSET)

        _chart_settings = d.pop("chart_settings", UNSET)
        chart_settings: ChartSettings | Unset
        if isinstance(_chart_settings, Unset):
            chart_settings = UNSET
        else:
            chart_settings = ChartSettings.from_dict(_chart_settings)

        cost_report = cls(
            token=token,
            title=title,
            folder_token=folder_token,
            saved_filter_tokens=saved_filter_tokens,
            business_metric_tokens_with_metadata=business_metric_tokens_with_metadata,
            filter_=filter_,
            groupings=groupings,
            settings=settings,
            created_at=created_at,
            workspace_token=workspace_token,
            previous_period_start_date=previous_period_start_date,
            previous_period_end_date=previous_period_end_date,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            chart_type=chart_type,
            date_bin=date_bin,
            chart_settings=chart_settings,
        )

        cost_report.additional_properties = d
        return cost_report

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
