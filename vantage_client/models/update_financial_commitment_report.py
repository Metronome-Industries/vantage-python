import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_financial_commitment_report_date_bucket import UpdateFinancialCommitmentReportDateBucket
from ..models.update_financial_commitment_report_date_interval import UpdateFinancialCommitmentReportDateInterval
from ..models.update_financial_commitment_report_on_demand_costs_scope import (
    UpdateFinancialCommitmentReportOnDemandCostsScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFinancialCommitmentReport")


@_attrs_define
class UpdateFinancialCommitmentReport:
    """Update a FinancialCommitmentReport.

    Attributes:
        title (Union[Unset, str]): The title of the FinancialCommitmentReport.
        filter_ (Union[Unset, str]): The filter query language to apply to the FinancialCommitmentReport. Additional
            documentation available at https://docs.vantage.sh/vql.
        start_date (Union[Unset, datetime.date]): The start date of the FinancialCommitmentReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter. Example: 2024-03-01.
        end_date (Union[Unset, datetime.date]): The end date of the FinancialCommitmentReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter. Example: 2024-03-01.
        date_interval (Union[Unset, UpdateFinancialCommitmentReportDateInterval]): The date interval of the
            FinancialCommitmentReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date'
            parameters. Defaults to 'last_3_months'.
        date_bucket (Union[Unset, UpdateFinancialCommitmentReportDateBucket]): The date bucket of the
            FinancialCommitmentReport.
        on_demand_costs_scope (Union[Unset, UpdateFinancialCommitmentReportOnDemandCostsScope]): The scope for the
            costs. Possible values: discountable, all.
        groupings (Union[Unset, list[str]]): Grouping values for aggregating costs on the FinancialCommitmentReport.
            Valid groupings: cost_type, commitment_type, service, resource_account_id, provider_account_id, region,
            cost_category, cost_sub_category, instance_type, tag, tag:<label_name>.
    """

    title: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    date_interval: Union[Unset, UpdateFinancialCommitmentReportDateInterval] = UNSET
    date_bucket: Union[Unset, UpdateFinancialCommitmentReportDateBucket] = UNSET
    on_demand_costs_scope: Union[Unset, UpdateFinancialCommitmentReportOnDemandCostsScope] = UNSET
    groupings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        filter_ = self.filter_

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        date_interval: Union[Unset, str] = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        date_bucket: Union[Unset, str] = UNSET
        if not isinstance(self.date_bucket, Unset):
            date_bucket = self.date_bucket.value

        on_demand_costs_scope: Union[Unset, str] = UNSET
        if not isinstance(self.on_demand_costs_scope, Unset):
            on_demand_costs_scope = self.on_demand_costs_scope.value

        groupings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groupings, Unset):
            groupings = self.groupings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if date_bucket is not UNSET:
            field_dict["date_bucket"] = date_bucket
        if on_demand_costs_scope is not UNSET:
            field_dict["on_demand_costs_scope"] = on_demand_costs_scope
        if groupings is not UNSET:
            field_dict["groupings"] = groupings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        filter_ = d.pop("filter", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: Union[Unset, UpdateFinancialCommitmentReportDateInterval]
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = UpdateFinancialCommitmentReportDateInterval(_date_interval)

        _date_bucket = d.pop("date_bucket", UNSET)
        date_bucket: Union[Unset, UpdateFinancialCommitmentReportDateBucket]
        if isinstance(_date_bucket, Unset):
            date_bucket = UNSET
        else:
            date_bucket = UpdateFinancialCommitmentReportDateBucket(_date_bucket)

        _on_demand_costs_scope = d.pop("on_demand_costs_scope", UNSET)
        on_demand_costs_scope: Union[Unset, UpdateFinancialCommitmentReportOnDemandCostsScope]
        if isinstance(_on_demand_costs_scope, Unset):
            on_demand_costs_scope = UNSET
        else:
            on_demand_costs_scope = UpdateFinancialCommitmentReportOnDemandCostsScope(_on_demand_costs_scope)

        groupings = cast(list[str], d.pop("groupings", UNSET))

        update_financial_commitment_report = cls(
            title=title,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            date_bucket=date_bucket,
            on_demand_costs_scope=on_demand_costs_scope,
            groupings=groupings,
        )

        update_financial_commitment_report.additional_properties = d
        return update_financial_commitment_report

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
