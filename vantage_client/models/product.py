from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_details import ProductDetails


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """Product model

    Attributes:
        id (Union[Unset, str]):
        category (Union[Unset, str]): The category of the cloud product Example: compute.
        name (Union[Unset, str]): The common name of the product. Example: EC2.
        service_id (Union[Unset, str]): A unique slug for the service the product belongs to. Example: aws-ec2.
        provider_id (Union[Unset, str]): A unique slug for the provider the product belongs to. Example: aws.
        details (Union[Unset, ProductDetails]): An object of metadata about the product. Example: {'gpu': 0, 'name': 'M5
            General Purpose 16xlarge', 'vcpu': 64, 'memory': 256, 'clock_speed_ghz': 3.1, 'physical_processor_description':
            'Intel Xeon Platinum 8175 (Skylake)', 'network_performance_description': '20 Gigabit'}.
    """

    id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    provider_id: Union[Unset, str] = UNSET
    details: Union[Unset, "ProductDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        name = self.name

        service_id = self.service_id

        provider_id = self.provider_id

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.product_details import ProductDetails

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        service_id = d.pop("service_id", UNSET)

        provider_id = d.pop("provider_id", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, ProductDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ProductDetails.from_dict(_details)

        product = cls(
            id=id,
            category=category,
            name=name,
            service_id=service_id,
            provider_id=provider_id,
            details=details,
        )

        product.additional_properties = d
        return product

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
