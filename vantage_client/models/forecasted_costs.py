from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forecasted_cost import ForecastedCost
    from ..models.forecasted_costs_links import ForecastedCostsLinks


T = TypeVar("T", bound="ForecastedCosts")


@_attrs_define
class ForecastedCosts:
    """ForecastedCosts model

    Attributes:
        links (Union[Unset, ForecastedCostsLinks]):
        forecasted_costs (Union[Unset, list['ForecastedCost']]):
        currency (Union[Unset, str]): The currency of the forecasted costs. Example: USD.
    """

    links: Union[Unset, "ForecastedCostsLinks"] = UNSET
    forecasted_costs: Union[Unset, list["ForecastedCost"]] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        forecasted_costs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.forecasted_costs, Unset):
            forecasted_costs = []
            for forecasted_costs_item_data in self.forecasted_costs:
                forecasted_costs_item = forecasted_costs_item_data.to_dict()
                forecasted_costs.append(forecasted_costs_item)

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if forecasted_costs is not UNSET:
            field_dict["forecasted_costs"] = forecasted_costs
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forecasted_cost import ForecastedCost
        from ..models.forecasted_costs_links import ForecastedCostsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, ForecastedCostsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ForecastedCostsLinks.from_dict(_links)

        forecasted_costs = []
        _forecasted_costs = d.pop("forecasted_costs", UNSET)
        for forecasted_costs_item_data in _forecasted_costs or []:
            forecasted_costs_item = ForecastedCost.from_dict(forecasted_costs_item_data)

            forecasted_costs.append(forecasted_costs_item)

        currency = d.pop("currency", UNSET)

        forecasted_costs = cls(
            links=links,
            forecasted_costs=forecasted_costs,
            currency=currency,
        )

        forecasted_costs.additional_properties = d
        return forecasted_costs

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
