from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_kubernetes_efficiency_report_aggregated_by import UpdateKubernetesEfficiencyReportAggregatedBy
from ..models.update_kubernetes_efficiency_report_date_bucket import UpdateKubernetesEfficiencyReportDateBucket
from ..models.update_kubernetes_efficiency_report_date_interval import UpdateKubernetesEfficiencyReportDateInterval
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKubernetesEfficiencyReport")


@_attrs_define
class UpdateKubernetesEfficiencyReport:
    """Update a KubernetesEfficiencyReport.

    Attributes:
        title (str | Unset): The title of the KubernetesEfficiencyReport.
        filter_ (str | Unset): The filter query language to apply to the KubernetesEfficiencyReport. Additional
            documentation available at https://docs.vantage.sh/vql.
        start_date (datetime.date | Unset): The start date of the KubernetesEfficiencyReport. ISO 8601 Formatted.
            Incompatible with 'date_interval' parameter.
        end_date (datetime.date | Unset): The end date of the KubernetesEfficiencyReport. ISO 8601 Formatted.
            Incompatible with 'date_interval' parameter.
        date_interval (UpdateKubernetesEfficiencyReportDateInterval | Unset): The date interval of the
            KubernetesEfficiencyReport. Incompatible with 'start_date' and 'end_date' parameters. Defaults to 'this_month'
            if start_date and end_date are not provided.
        aggregated_by (UpdateKubernetesEfficiencyReportAggregatedBy | Unset): The column by which the costs are
            aggregated.
        date_bucket (UpdateKubernetesEfficiencyReportDateBucket | Unset): The date bucket of the
            KubernetesEfficiencyReport.
        groupings (list[str] | Unset): Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid
            groupings: cluster_id, namespace, labeled, category, pod, label, label:<label_name>.
    """

    title: str | Unset = UNSET
    filter_: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    date_interval: UpdateKubernetesEfficiencyReportDateInterval | Unset = UNSET
    aggregated_by: UpdateKubernetesEfficiencyReportAggregatedBy | Unset = UNSET
    date_bucket: UpdateKubernetesEfficiencyReportDateBucket | Unset = UNSET
    groupings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        aggregated_by: str | Unset = UNSET
        if not isinstance(self.aggregated_by, Unset):
            aggregated_by = self.aggregated_by.value

        date_bucket: str | Unset = UNSET
        if not isinstance(self.date_bucket, Unset):
            date_bucket = self.date_bucket.value

        groupings: list[str] | Unset = UNSET
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
        if aggregated_by is not UNSET:
            field_dict["aggregated_by"] = aggregated_by
        if date_bucket is not UNSET:
            field_dict["date_bucket"] = date_bucket
        if groupings is not UNSET:
            field_dict["groupings"] = groupings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

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
        date_interval: UpdateKubernetesEfficiencyReportDateInterval | Unset
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = UpdateKubernetesEfficiencyReportDateInterval(_date_interval)

        _aggregated_by = d.pop("aggregated_by", UNSET)
        aggregated_by: UpdateKubernetesEfficiencyReportAggregatedBy | Unset
        if isinstance(_aggregated_by, Unset):
            aggregated_by = UNSET
        else:
            aggregated_by = UpdateKubernetesEfficiencyReportAggregatedBy(_aggregated_by)

        _date_bucket = d.pop("date_bucket", UNSET)
        date_bucket: UpdateKubernetesEfficiencyReportDateBucket | Unset
        if isinstance(_date_bucket, Unset):
            date_bucket = UNSET
        else:
            date_bucket = UpdateKubernetesEfficiencyReportDateBucket(_date_bucket)

        groupings = cast(list[str], d.pop("groupings", UNSET))

        update_kubernetes_efficiency_report = cls(
            title=title,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            aggregated_by=aggregated_by,
            date_bucket=date_bucket,
            groupings=groupings,
        )

        update_kubernetes_efficiency_report.additional_properties = d
        return update_kubernetes_efficiency_report

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
