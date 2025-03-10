from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_cost_report_chart_type import CreateCostReportChartType
from ..models.create_cost_report_date_bin import CreateCostReportDateBin
from ..models.create_cost_report_date_interval import CreateCostReportDateInterval
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_cost_report_business_metric_tokens_with_metadata_item import (
        CreateCostReportBusinessMetricTokensWithMetadataItem,
    )
    from ..models.create_cost_report_settings import CreateCostReportSettings


T = TypeVar("T", bound="CreateCostReport")


@_attrs_define
class CreateCostReport:
    """Create a CostReport.

    Attributes:
        title (str): The title of the CostReport.
        previous_period_end_date (str): The previous period end date of the CostReport. ISO 8601 Formatted.
        end_date (str): The end date of the CostReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
        workspace_token (Union[Unset, str]): The token of the Workspace to add the Cost Report to. Ignored if
            'folder_token' is set. Required if the API token is associated with multiple Workspaces.
        groupings (Union[Unset, str]): Grouping values for aggregating costs on the report. Valid groupings: account_id,
            billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service,
            tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values:
            groupings=provider,service,region
        filter_ (Union[Unset, str]): The filter query language to apply to the CostReport. Additional documentation
            available at https://docs.vantage.sh/vql.
        saved_filter_tokens (Union[Unset, list[str]]): The tokens of the SavedFilters to apply to the CostReport.
        business_metric_tokens_with_metadata (Union[Unset,
            list['CreateCostReportBusinessMetricTokensWithMetadataItem']]): The tokens for any BusinessMetrics to attach to
            the CostReport, and the unit scale.
        folder_token (Union[Unset, str]): The token of the Folder to add the CostReport to. Determines the Workspace the
            report is assigned to.
        settings (Union[Unset, CreateCostReportSettings]): Report settings.
        previous_period_start_date (Union[Unset, str]): The previous period start date of the CostReport. ISO 8601
            Formatted.
        start_date (Union[Unset, str]): The start date of the CostReport. ISO 8601 Formatted. Incompatible with
            'date_interval' parameter.
        date_interval (Union[Unset, CreateCostReportDateInterval]): The date interval of the CostReport. Incompatible
            with 'start_date' and 'end_date' parameters. Defaults to 'this_month' if start_date and end_date are not
            provided.
        chart_type (Union[Unset, CreateCostReportChartType]): The chart type of the CostReport. Default:
            CreateCostReportChartType.LINE.
        date_bin (Union[Unset, CreateCostReportDateBin]): The date bin of the CostReport. Default:
            CreateCostReportDateBin.CUMULATIVE.
    """

    title: str
    previous_period_end_date: str
    end_date: str
    workspace_token: Union[Unset, str] = UNSET
    groupings: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    saved_filter_tokens: Union[Unset, list[str]] = UNSET
    business_metric_tokens_with_metadata: Union[Unset, list["CreateCostReportBusinessMetricTokensWithMetadataItem"]] = (
        UNSET
    )
    folder_token: Union[Unset, str] = UNSET
    settings: Union[Unset, "CreateCostReportSettings"] = UNSET
    previous_period_start_date: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    date_interval: Union[Unset, CreateCostReportDateInterval] = UNSET
    chart_type: Union[Unset, CreateCostReportChartType] = CreateCostReportChartType.LINE
    date_bin: Union[Unset, CreateCostReportDateBin] = CreateCostReportDateBin.CUMULATIVE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        previous_period_end_date = self.previous_period_end_date

        end_date = self.end_date

        workspace_token = self.workspace_token

        groupings = self.groupings

        filter_ = self.filter_

        saved_filter_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        business_metric_tokens_with_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.business_metric_tokens_with_metadata, Unset):
            business_metric_tokens_with_metadata = []
            for business_metric_tokens_with_metadata_item_data in self.business_metric_tokens_with_metadata:
                business_metric_tokens_with_metadata_item = business_metric_tokens_with_metadata_item_data.to_dict()
                business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        folder_token = self.folder_token

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        previous_period_start_date = self.previous_period_start_date

        start_date = self.start_date

        date_interval: Union[Unset, str] = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        date_bin: Union[Unset, str] = UNSET
        if not isinstance(self.date_bin, Unset):
            date_bin = self.date_bin.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "previous_period_end_date": previous_period_end_date,
                "end_date": end_date,
            }
        )
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens
        if business_metric_tokens_with_metadata is not UNSET:
            field_dict["business_metric_tokens_with_metadata"] = business_metric_tokens_with_metadata
        if folder_token is not UNSET:
            field_dict["folder_token"] = folder_token
        if settings is not UNSET:
            field_dict["settings"] = settings
        if previous_period_start_date is not UNSET:
            field_dict["previous_period_start_date"] = previous_period_start_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if chart_type is not UNSET:
            field_dict["chart_type"] = chart_type
        if date_bin is not UNSET:
            field_dict["date_bin"] = date_bin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_cost_report_business_metric_tokens_with_metadata_item import (
            CreateCostReportBusinessMetricTokensWithMetadataItem,
        )
        from ..models.create_cost_report_settings import CreateCostReportSettings

        d = src_dict.copy()
        title = d.pop("title")

        previous_period_end_date = d.pop("previous_period_end_date")

        end_date = d.pop("end_date")

        workspace_token = d.pop("workspace_token", UNSET)

        groupings = d.pop("groupings", UNSET)

        filter_ = d.pop("filter", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        business_metric_tokens_with_metadata = []
        _business_metric_tokens_with_metadata = d.pop("business_metric_tokens_with_metadata", UNSET)
        for business_metric_tokens_with_metadata_item_data in _business_metric_tokens_with_metadata or []:
            business_metric_tokens_with_metadata_item = CreateCostReportBusinessMetricTokensWithMetadataItem.from_dict(
                business_metric_tokens_with_metadata_item_data
            )

            business_metric_tokens_with_metadata.append(business_metric_tokens_with_metadata_item)

        folder_token = d.pop("folder_token", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, CreateCostReportSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = CreateCostReportSettings.from_dict(_settings)

        previous_period_start_date = d.pop("previous_period_start_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: Union[Unset, CreateCostReportDateInterval]
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = CreateCostReportDateInterval(_date_interval)

        _chart_type = d.pop("chart_type", UNSET)
        chart_type: Union[Unset, CreateCostReportChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = CreateCostReportChartType(_chart_type)

        _date_bin = d.pop("date_bin", UNSET)
        date_bin: Union[Unset, CreateCostReportDateBin]
        if isinstance(_date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = CreateCostReportDateBin(_date_bin)

        create_cost_report = cls(
            title=title,
            previous_period_end_date=previous_period_end_date,
            end_date=end_date,
            workspace_token=workspace_token,
            groupings=groupings,
            filter_=filter_,
            saved_filter_tokens=saved_filter_tokens,
            business_metric_tokens_with_metadata=business_metric_tokens_with_metadata,
            folder_token=folder_token,
            settings=settings,
            previous_period_start_date=previous_period_start_date,
            start_date=start_date,
            date_interval=date_interval,
            chart_type=chart_type,
            date_bin=date_bin,
        )

        create_cost_report.additional_properties = d
        return create_cost_report

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
