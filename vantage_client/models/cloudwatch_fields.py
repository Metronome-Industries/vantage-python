from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
        stat (Union[Unset, CloudwatchFieldsStat]): The time aggregation function used to import Cloudwatch metrics.
            Example: Average.
        region (Union[Unset, str]): The region used to import Cloudwatch metrics. Example: us-east-1.
        namespace (Union[Unset, str]): The namespace used to import Cloudwatch metrics. Example: AWS/EC2.
        metric_name (Union[Unset, str]): The metric name used to import Cloudwatch metrics. Example: CPUUtilization.
        dimensions (Union[Unset, list['CloudwatchDimension']]): The dimensions used to pull specific statistical data
            for Cloudwatch metrics.
        label_dimension (Union[Unset, str]): The dimension used to aggregate the Cloudwatch metrics.
    """

    stat: Union[Unset, CloudwatchFieldsStat] = UNSET
    region: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    metric_name: Union[Unset, str] = UNSET
    dimensions: Union[Unset, list["CloudwatchDimension"]] = UNSET
    label_dimension: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stat: Union[Unset, str] = UNSET
        if not isinstance(self.stat, Unset):
            stat = self.stat.value

        region = self.region

        namespace = self.namespace

        metric_name = self.metric_name

        dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
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
        stat: Union[Unset, CloudwatchFieldsStat]
        if isinstance(_stat, Unset):
            stat = UNSET
        else:
            stat = CloudwatchFieldsStat(_stat)

        region = d.pop("region", UNSET)

        namespace = d.pop("namespace", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for dimensions_item_data in _dimensions or []:
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
