from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_virtual_tag_config_values_item_cost_metric_aggregation import (
        UpdateVirtualTagConfigValuesItemCostMetricAggregation,
    )


T = TypeVar("T", bound="UpdateVirtualTagConfigValuesItemCostMetric")


@_attrs_define
class UpdateVirtualTagConfigValuesItemCostMetric:
    """
    Attributes:
        filter_ (str):
        aggregation (UpdateVirtualTagConfigValuesItemCostMetricAggregation):
    """

    filter_: str
    aggregation: "UpdateVirtualTagConfigValuesItemCostMetricAggregation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        aggregation = self.aggregation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "aggregation": aggregation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_virtual_tag_config_values_item_cost_metric_aggregation import (
            UpdateVirtualTagConfigValuesItemCostMetricAggregation,
        )

        d = src_dict.copy()
        filter_ = d.pop("filter")

        aggregation = UpdateVirtualTagConfigValuesItemCostMetricAggregation.from_dict(d.pop("aggregation"))

        update_virtual_tag_config_values_item_cost_metric = cls(
            filter_=filter_,
            aggregation=aggregation,
        )

        update_virtual_tag_config_values_item_cost_metric.additional_properties = d
        return update_virtual_tag_config_values_item_cost_metric

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
