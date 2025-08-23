from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_alert_event import CostAlertEvent
    from ..models.cost_alert_events_links import CostAlertEventsLinks


T = TypeVar("T", bound="CostAlertEvents")


@_attrs_define
class CostAlertEvents:
    """CostAlertEvents model

    Attributes:
        links (Union[Unset, CostAlertEventsLinks]):
        cost_alert_events (Union[Unset, list['CostAlertEvent']]):
    """

    links: Union[Unset, "CostAlertEventsLinks"] = UNSET
    cost_alert_events: Union[Unset, list["CostAlertEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        cost_alert_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cost_alert_events, Unset):
            cost_alert_events = []
            for cost_alert_events_item_data in self.cost_alert_events:
                cost_alert_events_item = cost_alert_events_item_data.to_dict()
                cost_alert_events.append(cost_alert_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if cost_alert_events is not UNSET:
            field_dict["cost_alert_events"] = cost_alert_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_alert_event import CostAlertEvent
        from ..models.cost_alert_events_links import CostAlertEventsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, CostAlertEventsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CostAlertEventsLinks.from_dict(_links)

        cost_alert_events = []
        _cost_alert_events = d.pop("cost_alert_events", UNSET)
        for cost_alert_events_item_data in _cost_alert_events or []:
            cost_alert_events_item = CostAlertEvent.from_dict(cost_alert_events_item_data)

            cost_alert_events.append(cost_alert_events_item)

        cost_alert_events = cls(
            links=links,
            cost_alert_events=cost_alert_events,
        )

        cost_alert_events.additional_properties = d
        return cost_alert_events

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
