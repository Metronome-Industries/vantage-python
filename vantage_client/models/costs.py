from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost import Cost
    from ..models.links import Links


T = TypeVar("T", bound="Costs")


@_attrs_define
class Costs:
    """Costs model

    Attributes:
        links (Union[Unset, Links]):
        total_cost (Union[Unset, str]): The sum of all costs for the CostReport for the requested period, rounded to 2
            decimal places, alongside the ISO 4217 currency code.
        total_usage (Union[Unset, str]): The sum of all usage for the CostReport for the requested period, rounded to 2
            decimal places, grouped by usage unit.
        costs (Union[Unset, list['Cost']]):
    """

    links: Union[Unset, "Links"] = UNSET
    total_cost: Union[Unset, str] = UNSET
    total_usage: Union[Unset, str] = UNSET
    costs: Union[Unset, list["Cost"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        total_cost = self.total_cost

        total_usage = self.total_usage

        costs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.costs, Unset):
            costs = []
            for costs_item_data in self.costs:
                costs_item = costs_item_data.to_dict()
                costs.append(costs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost
        if total_usage is not UNSET:
            field_dict["total_usage"] = total_usage
        if costs is not UNSET:
            field_dict["costs"] = costs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cost import Cost
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        total_cost = d.pop("total_cost", UNSET)

        total_usage = d.pop("total_usage", UNSET)

        costs = []
        _costs = d.pop("costs", UNSET)
        for costs_item_data in _costs or []:
            costs_item = Cost.from_dict(costs_item_data)

            costs.append(costs_item)

        costs = cls(
            links=links,
            total_cost=total_cost,
            total_usage=total_usage,
            costs=costs,
        )

        costs.additional_properties = d
        return costs

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
