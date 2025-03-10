from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductDetails")


@_attrs_define
class ProductDetails:
    """An object of metadata about the product.

    Example:
        {'gpu': 0, 'name': 'M5 General Purpose 16xlarge', 'vcpu': 64, 'memory': 256, 'clock_speed_ghz': 3.1,
            'physical_processor_description': 'Intel Xeon Platinum 8175 (Skylake)', 'network_performance_description': '20
            Gigabit'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        product_details = cls()

        product_details.additional_properties = d
        return product_details

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
