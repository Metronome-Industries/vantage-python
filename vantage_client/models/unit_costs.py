from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_cost import UnitCost
    from ..models.unit_costs_links import UnitCostsLinks


T = TypeVar("T", bound="UnitCosts")


@_attrs_define
class UnitCosts:
    """UnitCosts model

    Attributes:
        links (Union[Unset, UnitCostsLinks]):
        unit_costs (Union[Unset, list['UnitCost']]):
    """

    links: Union[Unset, "UnitCostsLinks"] = UNSET
    unit_costs: Union[Unset, list["UnitCost"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        unit_costs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.unit_costs, Unset):
            unit_costs = []
            for unit_costs_item_data in self.unit_costs:
                unit_costs_item = unit_costs_item_data.to_dict()
                unit_costs.append(unit_costs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if unit_costs is not UNSET:
            field_dict["unit_costs"] = unit_costs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_cost import UnitCost
        from ..models.unit_costs_links import UnitCostsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, UnitCostsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UnitCostsLinks.from_dict(_links)

        unit_costs = []
        _unit_costs = d.pop("unit_costs", UNSET)
        for unit_costs_item_data in _unit_costs or []:
            unit_costs_item = UnitCost.from_dict(unit_costs_item_data)

            unit_costs.append(unit_costs_item)

        unit_costs = cls(
            links=links,
            unit_costs=unit_costs,
        )

        unit_costs.additional_properties = d
        return unit_costs

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
