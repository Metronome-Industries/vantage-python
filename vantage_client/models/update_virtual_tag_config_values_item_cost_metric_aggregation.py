from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateVirtualTagConfigValuesItemCostMetricAggregation")


@_attrs_define
class UpdateVirtualTagConfigValuesItemCostMetricAggregation:
    """
    Attributes:
        tag (str):
    """

    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag")

        update_virtual_tag_config_values_item_cost_metric_aggregation = cls(
            tag=tag,
        )

        update_virtual_tag_config_values_item_cost_metric_aggregation.additional_properties = d
        return update_virtual_tag_config_values_item_cost_metric_aggregation

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
