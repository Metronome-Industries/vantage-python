from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeRate")


@_attrs_define
class ExchangeRate:
    """
    Attributes:
        base_currency_code (str | Unset):
        currency_code (str | Unset):
        rate (str | Unset):
        effective_date (str | Unset):
        updated_at (str | Unset):
    """

    base_currency_code: str | Unset = UNSET
    currency_code: str | Unset = UNSET
    rate: str | Unset = UNSET
    effective_date: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_currency_code = self.base_currency_code

        currency_code = self.currency_code

        rate = self.rate

        effective_date = self.effective_date

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_currency_code is not UNSET:
            field_dict["base_currency_code"] = base_currency_code
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if rate is not UNSET:
            field_dict["rate"] = rate
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_currency_code = d.pop("base_currency_code", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        rate = d.pop("rate", UNSET)

        effective_date = d.pop("effective_date", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        exchange_rate = cls(
            base_currency_code=base_currency_code,
            currency_code=currency_code,
            rate=rate,
            effective_date=effective_date,
            updated_at=updated_at,
        )

        exchange_rate.additional_properties = d
        return exchange_rate

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
