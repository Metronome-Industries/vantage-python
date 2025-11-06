from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_notification import AnomalyNotification
    from ..models.anomaly_notifications_links import AnomalyNotificationsLinks


T = TypeVar("T", bound="AnomalyNotifications")


@_attrs_define
class AnomalyNotifications:
    """AnomalyNotifications model

    Attributes:
        links (AnomalyNotificationsLinks | Unset):
        anomaly_notifications (list[AnomalyNotification] | Unset):
    """

    links: AnomalyNotificationsLinks | Unset = UNSET
    anomaly_notifications: list[AnomalyNotification] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        anomaly_notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.anomaly_notifications, Unset):
            anomaly_notifications = []
            for anomaly_notifications_item_data in self.anomaly_notifications:
                anomaly_notifications_item = anomaly_notifications_item_data.to_dict()
                anomaly_notifications.append(anomaly_notifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if anomaly_notifications is not UNSET:
            field_dict["anomaly_notifications"] = anomaly_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.anomaly_notification import AnomalyNotification
        from ..models.anomaly_notifications_links import AnomalyNotificationsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: AnomalyNotificationsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AnomalyNotificationsLinks.from_dict(_links)

        _anomaly_notifications = d.pop("anomaly_notifications", UNSET)
        anomaly_notifications: list[AnomalyNotification] | Unset = UNSET
        if _anomaly_notifications is not UNSET:
            anomaly_notifications = []
            for anomaly_notifications_item_data in _anomaly_notifications:
                anomaly_notifications_item = AnomalyNotification.from_dict(anomaly_notifications_item_data)

                anomaly_notifications.append(anomaly_notifications_item)

        anomaly_notifications = cls(
            links=links,
            anomaly_notifications=anomaly_notifications,
        )

        anomaly_notifications.additional_properties = d
        return anomaly_notifications

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
