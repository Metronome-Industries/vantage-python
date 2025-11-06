from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_financial_commitment_report_date_bucket import CreateFinancialCommitmentReportDateBucket
from ..models.create_financial_commitment_report_date_interval import CreateFinancialCommitmentReportDateInterval
from ..models.create_financial_commitment_report_on_demand_costs_scope import (
    CreateFinancialCommitmentReportOnDemandCostsScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFinancialCommitmentReport")


@_attrs_define
class CreateFinancialCommitmentReport:
    """Create a FinancialCommitmentReport.

    Attributes:
        workspace_token (str): The Workspace in which the FinancialCommitmentReport will be created.
        title (str): The title of the FinancialCommitmentReport.
        filter_ (str | Unset): The filter query language to apply to the FinancialCommitmentReport. Additional
            documentation available at https://docs.vantage.sh/vql.
        start_date (datetime.date | Unset): The start date of the FinancialCommitmentReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter. Example: 2024-03-01.
        end_date (datetime.date | Unset): The end date of the FinancialCommitmentReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter. Example: 2024-03-01.
        date_interval (CreateFinancialCommitmentReportDateInterval | Unset): The date interval of the
            FinancialCommitmentReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date'
            parameters. Defaults to 'last_3_months'.
        date_bucket (CreateFinancialCommitmentReportDateBucket | Unset): The date bucket of the
            FinancialCommitmentReport.
        on_demand_costs_scope (CreateFinancialCommitmentReportOnDemandCostsScope | Unset): The scope for the costs.
            Possible values: discountable, all.
        groupings (list[str] | Unset): Grouping values for aggregating costs on the FinancialCommitmentReport. Valid
            groupings: cost_type, commitment_type, service, resource_account_id, provider_account_id, region, cost_category,
            cost_sub_category, instance_type, tag, tag:<label_name>.
    """

    workspace_token: str
    title: str
    filter_: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    date_interval: CreateFinancialCommitmentReportDateInterval | Unset = UNSET
    date_bucket: CreateFinancialCommitmentReportDateBucket | Unset = UNSET
    on_demand_costs_scope: CreateFinancialCommitmentReportOnDemandCostsScope | Unset = UNSET
    groupings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_token = self.workspace_token

        title = self.title

        filter_ = self.filter_

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        date_interval: str | Unset = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        date_bucket: str | Unset = UNSET
        if not isinstance(self.date_bucket, Unset):
            date_bucket = self.date_bucket.value

        on_demand_costs_scope: str | Unset = UNSET
        if not isinstance(self.on_demand_costs_scope, Unset):
            on_demand_costs_scope = self.on_demand_costs_scope.value

        groupings: list[str] | Unset = UNSET
        if not isinstance(self.groupings, Unset):
            groupings = self.groupings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_token": workspace_token,
                "title": title,
            }
        )
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_token = d.pop("workspace_token")

        title = d.pop("title")

        filter_ = d.pop("filter", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: CreateFinancialCommitmentReportDateInterval | Unset
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = CreateFinancialCommitmentReportDateInterval(_date_interval)

        _date_bucket = d.pop("date_bucket", UNSET)
        date_bucket: CreateFinancialCommitmentReportDateBucket | Unset
        if isinstance(_date_bucket, Unset):
            date_bucket = UNSET
        else:
            date_bucket = CreateFinancialCommitmentReportDateBucket(_date_bucket)

        _on_demand_costs_scope = d.pop("on_demand_costs_scope", UNSET)
        on_demand_costs_scope: CreateFinancialCommitmentReportOnDemandCostsScope | Unset
        if isinstance(_on_demand_costs_scope, Unset):
            on_demand_costs_scope = UNSET
        else:
            on_demand_costs_scope = CreateFinancialCommitmentReportOnDemandCostsScope(_on_demand_costs_scope)

        groupings = cast(list[str], d.pop("groupings", UNSET))

        create_financial_commitment_report = cls(
            workspace_token=workspace_token,
            title=title,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            date_bucket=date_bucket,
            on_demand_costs_scope=on_demand_costs_scope,
            groupings=groupings,
        )

        create_financial_commitment_report.additional_properties = d
        return create_financial_commitment_report

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
