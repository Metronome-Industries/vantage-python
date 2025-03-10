from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_alert import BudgetAlert
    from ..models.links import Links


T = TypeVar("T", bound="BudgetAlerts")


@_attrs_define
class BudgetAlerts:
    """BudgetAlerts model

    Attributes:
        links (Union[Unset, Links]):
        budget_alerts (Union[Unset, list['BudgetAlert']]):
    """

    links: Union[Unset, "Links"] = UNSET
    budget_alerts: Union[Unset, list["BudgetAlert"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        budget_alerts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.budget_alerts, Unset):
            budget_alerts = []
            for budget_alerts_item_data in self.budget_alerts:
                budget_alerts_item = budget_alerts_item_data.to_dict()
                budget_alerts.append(budget_alerts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if budget_alerts is not UNSET:
            field_dict["budget_alerts"] = budget_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.budget_alert import BudgetAlert
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        budget_alerts = []
        _budget_alerts = d.pop("budget_alerts", UNSET)
        for budget_alerts_item_data in _budget_alerts or []:
            budget_alerts_item = BudgetAlert.from_dict(budget_alerts_item_data)

            budget_alerts.append(budget_alerts_item)

        budget_alerts = cls(
            links=links,
            budget_alerts=budget_alerts,
        )

        budget_alerts.additional_properties = d
        return budget_alerts

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
