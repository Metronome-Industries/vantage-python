from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_metric import BusinessMetric


T = TypeVar("T", bound="BusinessMetrics")


@_attrs_define
class BusinessMetrics:
    """BusinessMetrics model

    Attributes:
        business_metrics (Union[Unset, list['BusinessMetric']]):
    """

    business_metrics: Union[Unset, list["BusinessMetric"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_metrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.business_metrics, Unset):
            business_metrics = []
            for business_metrics_item_data in self.business_metrics:
                business_metrics_item = business_metrics_item_data.to_dict()
                business_metrics.append(business_metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_metrics is not UNSET:
            field_dict["business_metrics"] = business_metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.business_metric import BusinessMetric

        d = src_dict.copy()
        business_metrics = []
        _business_metrics = d.pop("business_metrics", UNSET)
        for business_metrics_item_data in _business_metrics or []:
            business_metrics_item = BusinessMetric.from_dict(business_metrics_item_data)

            business_metrics.append(business_metrics_item)

        business_metrics = cls(
            business_metrics=business_metrics,
        )

        business_metrics.additional_properties = d
        return business_metrics

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
