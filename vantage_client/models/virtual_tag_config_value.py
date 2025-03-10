from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_config_value_cost_metric import VirtualTagConfigValueCostMetric


T = TypeVar("T", bound="VirtualTagConfigValue")


@_attrs_define
class VirtualTagConfigValue:
    """
    Attributes:
        filter_ (Union[Unset, str]): The filter VQL for the Value. Example: costs.provider = 'aws' AND costs.service =
            'Amazon Simple Storage Service'.
        name (Union[Unset, str]): The name of the Value. Example: Informatics.
        business_metric_token (Union[Unset, str]): The token of the associated BusinessMetric. Example:
            bsnss_mtrc_abc123.
        cost_metric (Union[Unset, VirtualTagConfigValueCostMetric]):
    """

    filter_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    business_metric_token: Union[Unset, str] = UNSET
    cost_metric: Union[Unset, "VirtualTagConfigValueCostMetric"] = UNSET
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
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if name is not UNSET:
            field_dict["name"] = name
        if business_metric_token is not UNSET:
            field_dict["business_metric_token"] = business_metric_token
        if cost_metric is not UNSET:
            field_dict["cost_metric"] = cost_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.virtual_tag_config_value_cost_metric import VirtualTagConfigValueCostMetric

        d = src_dict.copy()
        filter_ = d.pop("filter", UNSET)

        name = d.pop("name", UNSET)

        business_metric_token = d.pop("business_metric_token", UNSET)

        _cost_metric = d.pop("cost_metric", UNSET)
        cost_metric: Union[Unset, VirtualTagConfigValueCostMetric]
        if isinstance(_cost_metric, Unset):
            cost_metric = UNSET
        else:
            cost_metric = VirtualTagConfigValueCostMetric.from_dict(_cost_metric)

        virtual_tag_config_value = cls(
            filter_=filter_,
            name=name,
            business_metric_token=business_metric_token,
            cost_metric=cost_metric,
        )

        virtual_tag_config_value.additional_properties = d
        return virtual_tag_config_value

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
