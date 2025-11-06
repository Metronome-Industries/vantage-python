from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloudwatch_fields_stat import CloudwatchFieldsStat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloudwatch_dimension import CloudwatchDimension


T = TypeVar("T", bound="CloudwatchFields")


@_attrs_define
class CloudwatchFields:
    """
    Attributes:
        stat (CloudwatchFieldsStat | Unset): The time aggregation function used to import Cloudwatch metrics. Example:
            Average.
        region (str | Unset): The region used to import Cloudwatch metrics. Example: us-east-1.
        namespace (str | Unset): The namespace used to import Cloudwatch metrics. Example: AWS/EC2.
        metric_name (str | Unset): The metric name used to import Cloudwatch metrics. Example: CPUUtilization.
        dimensions (list[CloudwatchDimension] | Unset): The dimensions used to pull specific statistical data for
            Cloudwatch metrics.
        label_dimension (str | Unset): The dimension used to aggregate the Cloudwatch metrics.
    """

    stat: CloudwatchFieldsStat | Unset = UNSET
    region: str | Unset = UNSET
    namespace: str | Unset = UNSET
    metric_name: str | Unset = UNSET
    dimensions: list[CloudwatchDimension] | Unset = UNSET
    label_dimension: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stat: str | Unset = UNSET
        if not isinstance(self.stat, Unset):
            stat = self.stat.value

        region = self.region

        namespace = self.namespace

        metric_name = self.metric_name

        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        label_dimension = self.label_dimension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stat is not UNSET:
            field_dict["stat"] = stat
        if region is not UNSET:
            field_dict["region"] = region
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if metric_name is not UNSET:
            field_dict["metric_name"] = metric_name
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if label_dimension is not UNSET:
            field_dict["label_dimension"] = label_dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloudwatch_dimension import CloudwatchDimension

        d = dict(src_dict)
        _stat = d.pop("stat", UNSET)
        stat: CloudwatchFieldsStat | Unset
        if isinstance(_stat, Unset):
            stat = UNSET
        else:
            stat = CloudwatchFieldsStat(_stat)

        region = d.pop("region", UNSET)

        namespace = d.pop("namespace", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[CloudwatchDimension] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = CloudwatchDimension.from_dict(dimensions_item_data)

                dimensions.append(dimensions_item)

        label_dimension = d.pop("label_dimension", UNSET)

        cloudwatch_fields = cls(
            stat=stat,
            region=region,
            namespace=namespace,
            metric_name=metric_name,
            dimensions=dimensions,
            label_dimension=label_dimension,
        )

        cloudwatch_fields.additional_properties = d
        return cloudwatch_fields

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
