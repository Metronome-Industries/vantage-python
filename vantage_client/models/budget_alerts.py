from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_alert import BudgetAlert
    from ..models.budget_alerts_links import BudgetAlertsLinks


T = TypeVar("T", bound="BudgetAlerts")


@_attrs_define
class BudgetAlerts:
    """BudgetAlerts model

    Attributes:
        links (BudgetAlertsLinks | Unset):
        budget_alerts (list[BudgetAlert] | Unset):
    """

    links: BudgetAlertsLinks | Unset = UNSET
    budget_alerts: list[BudgetAlert] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        budget_alerts: list[dict[str, Any]] | Unset = UNSET
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_alert import BudgetAlert
        from ..models.budget_alerts_links import BudgetAlertsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: BudgetAlertsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BudgetAlertsLinks.from_dict(_links)

        _budget_alerts = d.pop("budget_alerts", UNSET)
        budget_alerts: list[BudgetAlert] | Unset = UNSET
        if _budget_alerts is not UNSET:
            budget_alerts = []
            for budget_alerts_item_data in _budget_alerts:
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
