from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_service import CostService
    from ..models.cost_services_links import CostServicesLinks


T = TypeVar("T", bound="CostServices")


@_attrs_define
class CostServices:
    """CostServices model

    Attributes:
        links (Union[Unset, CostServicesLinks]):
        cost_services (Union[Unset, list['CostService']]):
    """

    links: Union[Unset, "CostServicesLinks"] = UNSET
    cost_services: Union[Unset, list["CostService"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        cost_services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cost_services, Unset):
            cost_services = []
            for cost_services_item_data in self.cost_services:
                cost_services_item = cost_services_item_data.to_dict()
                cost_services.append(cost_services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if cost_services is not UNSET:
            field_dict["cost_services"] = cost_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_service import CostService
        from ..models.cost_services_links import CostServicesLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, CostServicesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CostServicesLinks.from_dict(_links)

        cost_services = []
        _cost_services = d.pop("cost_services", UNSET)
        for cost_services_item_data in _cost_services or []:
            cost_services_item = CostService.from_dict(cost_services_item_data)

            cost_services.append(cost_services_item)

        cost_services = cls(
            links=links,
            cost_services=cost_services,
        )

        cost_services.additional_properties = d
        return cost_services

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
