from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_metric_value import BusinessMetricValue


T = TypeVar("T", bound="BusinessMetricValues")


@_attrs_define
class BusinessMetricValues:
    """BusinessMetricValues model

    Attributes:
        values (Union[Unset, list['BusinessMetricValue']]):
    """

    values: Union[Unset, list["BusinessMetricValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.business_metric_value import BusinessMetricValue

        d = src_dict.copy()
        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = BusinessMetricValue.from_dict(values_item_data)

            values.append(values_item)

        business_metric_values = cls(
            values=values,
        )

        business_metric_values.additional_properties = d
        return business_metric_values

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
