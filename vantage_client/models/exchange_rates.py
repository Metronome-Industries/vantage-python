from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_rate import ExchangeRate
    from ..models.exchange_rates_links import ExchangeRatesLinks


T = TypeVar("T", bound="ExchangeRates")


@_attrs_define
class ExchangeRates:
    """ExchangeRates model

    Attributes:
        links (ExchangeRatesLinks | Unset):
        exchange_rates (list[ExchangeRate] | Unset):
    """

    links: ExchangeRatesLinks | Unset = UNSET
    exchange_rates: list[ExchangeRate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        exchange_rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exchange_rates, Unset):
            exchange_rates = []
            for exchange_rates_item_data in self.exchange_rates:
                exchange_rates_item = exchange_rates_item_data.to_dict()
                exchange_rates.append(exchange_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if exchange_rates is not UNSET:
            field_dict["exchange_rates"] = exchange_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_rate import ExchangeRate
        from ..models.exchange_rates_links import ExchangeRatesLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: ExchangeRatesLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ExchangeRatesLinks.from_dict(_links)

        _exchange_rates = d.pop("exchange_rates", UNSET)
        exchange_rates: list[ExchangeRate] | Unset = UNSET
        if _exchange_rates is not UNSET:
            exchange_rates = []
            for exchange_rates_item_data in _exchange_rates:
                exchange_rates_item = ExchangeRate.from_dict(exchange_rates_item_data)

                exchange_rates.append(exchange_rates_item)

        exchange_rates = cls(
            links=links,
            exchange_rates=exchange_rates,
        )

        exchange_rates.additional_properties = d
        return exchange_rates

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
