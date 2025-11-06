from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.forecasted_cost_provider import ForecastedCostProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forecasted_cost_links import ForecastedCostLinks


T = TypeVar("T", bound="ForecastedCost")


@_attrs_define
class ForecastedCost:
    """
    Attributes:
        links (ForecastedCostLinks | Unset):
        date (str | Unset): The date the forecasted cost is projected to accrue. ISO 8601 Formatted. Example:
            2035-09-05+00:00.
        amount (str | Unset): The amount of the forecasted cost. Example: 4.25.
        provider (ForecastedCostProvider | Unset): The cost provider which incurred the cost. Will be 'all' for all
            combined providers. Example: aws.
        service (str | Unset): The service for the forecasted cost. Will be 'all' for all combined services Example:
            Amazon Elastic Compute Cloud - Compute.
    """

    links: ForecastedCostLinks | Unset = UNSET
    date: str | Unset = UNSET
    amount: str | Unset = UNSET
    provider: ForecastedCostProvider | Unset = UNSET
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        date = self.date

        amount = self.amount

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if provider is not UNSET:
            field_dict["provider"] = provider
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forecasted_cost_links import ForecastedCostLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: ForecastedCostLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ForecastedCostLinks.from_dict(_links)

        date = d.pop("date", UNSET)

        amount = d.pop("amount", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ForecastedCostProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ForecastedCostProvider(_provider)

        service = d.pop("service", UNSET)

        forecasted_cost = cls(
            links=links,
            date=date,
            amount=amount,
            provider=provider,
            service=service,
        )

        forecasted_cost.additional_properties = d
        return forecasted_cost

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
