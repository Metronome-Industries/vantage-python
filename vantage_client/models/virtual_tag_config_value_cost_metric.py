from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_config_value_cost_metric_aggregation import VirtualTagConfigValueCostMetricAggregation


T = TypeVar("T", bound="VirtualTagConfigValueCostMetric")


@_attrs_define
class VirtualTagConfigValueCostMetric:
    """
    Attributes:
        filter_ (str | Unset): The filter VQL for the cost metric.
        aggregation (VirtualTagConfigValueCostMetricAggregation | Unset):
    """

    filter_: str | Unset = UNSET
    aggregation: VirtualTagConfigValueCostMetricAggregation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        aggregation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_tag_config_value_cost_metric_aggregation import VirtualTagConfigValueCostMetricAggregation

        d = dict(src_dict)
        filter_ = d.pop("filter", UNSET)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: VirtualTagConfigValueCostMetricAggregation | Unset
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = VirtualTagConfigValueCostMetricAggregation.from_dict(_aggregation)

        virtual_tag_config_value_cost_metric = cls(
            filter_=filter_,
            aggregation=aggregation,
        )

        virtual_tag_config_value_cost_metric.additional_properties = d
        return virtual_tag_config_value_cost_metric

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
