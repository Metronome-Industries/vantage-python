from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_business_metric_for_cost_report import AttachedBusinessMetricForCostReport
    from ..models.cost_report_settings import CostReportSettings


T = TypeVar("T", bound="CostReport")


@_attrs_define
class CostReport:
    """CostReport model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the CostReport. Example: Production Environment.
        folder_token (Union[Unset, str]): The token for the Folder the CostReport is a part of.
        saved_filter_tokens (Union[Unset, list[str]]): The tokens for the SavedFilters assigned to the CostReport.
        business_metric_tokens_with_metadata (Union[Unset, list['AttachedBusinessMetricForCostReport']]): The tokens for
            the BusinessMetrics assigned to the CostReport, the unit scale, and label filter.
        filter_ (Union[Unset, str]): The filter applied to the CostReport. Additional documentation available at
            https://docs.vantage.sh/vql.
        groupings (Union[Unset, str]): The grouping aggregations applied to the filtered data. Example: provider,
            service.
        settings (Union[Unset, CostReportSettings]): Report settings.
        created_at (Union[Unset, str]): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2021-07-09 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the CostReport is a part of.
        previous_period_start_date (Union[Unset, str]): The previous period start date of the CostReport. ISO 8601
            Formatted. Example: 2024-06-01.
        previous_period_end_date (Union[Unset, str]): The previous period end date of the CostReport. ISO 8601
            Formatted. Example: 2024-06-15.
        start_date (Union[Unset, str]): The start date of the CostReports. ISO 8601 Formatted. Overwrites
            'date_interval' if set. Example: 2024-07-01.
        end_date (Union[Unset, str]): The end date of the CostReports. ISO 8601 Formatted. Overwrites 'date_interval' if
            set. Example: 2024-07-15.
        date_interval (Union[Unset, str]): The date interval of the CostReport.
        chart_type (Union[Unset, str]): The chart type of the CostReport.
        date_bin (Union[Unset, str]): The date bin of the CostReport.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    folder_token: Union[Unset, str] = UNSET
    saved_filter_tokens: Union[Unset, list[str]] = UNSET
    business_metric_tokens_with_metadata: Union[Unset, list["AttachedBusinessMetricForCostReport"]] = UNSET
    filter_: Union[Unset, str] = UNSET
    groupings: Union[Unset, str] = UNSET
    settings: Union[Unset, "CostReportSettings"] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    previous_period_start_date: Union[Unset, str] = UNSET
    previous_period_end_date: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    date_interval: Union[Unset, str] = UNSET
    chart_type: Union[Unset, str] = UNSET
    date_bin: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        folder_token = self.folder_token

        saved_filter_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        business_metric_tokens_with_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.business_metric_tokens_with_metadata, Unset):
            business_metric_tokens_with_metadata = []
            for business_metric_tokens_with_metadata_item_data in self.business_metric_tokens_with_metadata:
                business_metric_tokens_with_metadata_item = business_metric_tokens_with_metadata_item_data.to_dict()
                business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        filter_ = self.filter_

        groupings = self.groupings

        settings: Union[Unset, dict[str, Any]] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attached_business_metric_for_cost_report import AttachedBusinessMetricForCostReport
        from ..models.cost_report_settings import CostReportSettings

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        folder_token = d.pop("folder_token", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        business_metric_tokens_with_metadata = []
        _business_metric_tokens_with_metadata = d.pop("business_metric_tokens_with_metadata", UNSET)
        for business_metric_tokens_with_metadata_item_data in _business_metric_tokens_with_metadata or []:
            business_metric_tokens_with_metadata_item = AttachedBusinessMetricForCostReport.from_dict(
                business_metric_tokens_with_metadata_item_data
            )

            business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        filter_ = d.pop("filter", UNSET)

        groupings = d.pop("groupings", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, CostReportSettings]
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
