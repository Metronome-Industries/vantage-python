from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_virtual_tag_config_values_item_cost_metric import UpdateVirtualTagConfigValuesItemCostMetric


T = TypeVar("T", bound="UpdateVirtualTagConfigValuesItem")


@_attrs_define
class UpdateVirtualTagConfigValuesItem:
    """
    Attributes:
        filter_ (str): The filter query language to apply to the value. Additional documentation available at
            https://docs.vantage.sh/vql.
        name (Union[Unset, str]): The name of the value.
        business_metric_token (Union[Unset, str]): The token of an associated business metric.
        cost_metric (Union[Unset, UpdateVirtualTagConfigValuesItemCostMetric]):
    """

    filter_: str
    name: Union[Unset, str] = UNSET
    business_metric_token: Union[Unset, str] = UNSET
    cost_metric: Union[Unset, "UpdateVirtualTagConfigValuesItemCostMetric"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        name = self.name

        business_metric_token = self.business_metric_token

        cost_metric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cost_metric, Unset):
            cost_metric = self.cost_metric.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if business_metric_token is not UNSET:
            field_dict["business_metric_token"] = business_metric_token
        if cost_metric is not UNSET:
            field_dict["cost_metric"] = cost_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_virtual_tag_config_values_item_cost_metric import (
            UpdateVirtualTagConfigValuesItemCostMetric,
        )

        d = src_dict.copy()
        filter_ = d.pop("filter")

        name = d.pop("name", UNSET)

        business_metric_token = d.pop("business_metric_token", UNSET)

        _cost_metric = d.pop("cost_metric", UNSET)
        cost_metric: Union[Unset, UpdateVirtualTagConfigValuesItemCostMetric]
        if isinstance(_cost_metric, Unset):
            cost_metric = UNSET
        else:
            cost_metric = UpdateVirtualTagConfigValuesItemCostMetric.from_dict(_cost_metric)

        update_virtual_tag_config_values_item = cls(
            filter_=filter_,
            name=name,
            business_metric_token=business_metric_token,
            cost_metric=cost_metric,
        )

        update_virtual_tag_config_values_item.additional_properties = d
        return update_virtual_tag_config_values_item

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
