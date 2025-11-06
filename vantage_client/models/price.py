from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_details import PriceDetails


T = TypeVar("T", bound="Price")


@_attrs_define
class Price:
    """Price model

    Attributes:
        id (str | Unset):
        unit (str | Unset): The unit in which the amount is billed. Example: hour.
        region (str | Unset): The region the price is specific to. Example: us-east-1.
        rate_type (str | Unset): The part of the product the price applies to. (compute, transfer, etc..) Example:
            compute.
        currency (str | Unset): The currency of the amount. Example: USD.
        amount (float | Unset): The amount of money this specific product price costs. Example: 1.324.
        details (PriceDetails | Unset): Service specific metadata. Example: {'platform': 'linux-enterprise',
            'lifecycle': 'on-demand'}.
    """

    id: str | Unset = UNSET
    unit: str | Unset = UNSET
    region: str | Unset = UNSET
    rate_type: str | Unset = UNSET
    currency: str | Unset = UNSET
    amount: float | Unset = UNSET
    details: PriceDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        unit = self.unit

        region = self.region

        rate_type = self.rate_type

        currency = self.currency

        amount = self.amount

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if unit is not UNSET:
            field_dict["unit"] = unit
        if region is not UNSET:
            field_dict["region"] = region
        if rate_type is not UNSET:
            field_dict["rate_type"] = rate_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_details import PriceDetails

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        unit = d.pop("unit", UNSET)

        region = d.pop("region", UNSET)

        rate_type = d.pop("rate_type", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        _details = d.pop("details", UNSET)
        details: PriceDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PriceDetails.from_dict(_details)

        price = cls(
            id=id,
            unit=unit,
            region=region,
            rate_type=rate_type,
            currency=currency,
            amount=amount,
            details=details,
        )

        price.additional_properties = d
        return price

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
