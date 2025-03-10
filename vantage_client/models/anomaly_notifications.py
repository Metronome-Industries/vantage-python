from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_notification import AnomalyNotification
    from ..models.links import Links


T = TypeVar("T", bound="AnomalyNotifications")


@_attrs_define
class AnomalyNotifications:
    """AnomalyNotifications model

    Attributes:
        links (Union[Unset, Links]):
        anomaly_notifications (Union[Unset, list['AnomalyNotification']]):
    """

    links: Union[Unset, "Links"] = UNSET
    anomaly_notifications: Union[Unset, list["AnomalyNotification"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        anomaly_notifications: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.anomaly_notification import AnomalyNotification
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        anomaly_notifications = []
        _anomaly_notifications = d.pop("anomaly_notifications", UNSET)
        for anomaly_notifications_item_data in _anomaly_notifications or []:
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
