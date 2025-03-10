from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_alert import AnomalyAlert
    from ..models.links import Links


T = TypeVar("T", bound="AnomalyAlerts")


@_attrs_define
class AnomalyAlerts:
    """AnomalyAlerts model

    Attributes:
        links (Union[Unset, Links]):
        anomaly_alerts (Union[Unset, list['AnomalyAlert']]):
    """

    links: Union[Unset, "Links"] = UNSET
    anomaly_alerts: Union[Unset, list["AnomalyAlert"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        anomaly_alerts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.anomaly_alerts, Unset):
            anomaly_alerts = []
            for anomaly_alerts_item_data in self.anomaly_alerts:
                anomaly_alerts_item = anomaly_alerts_item_data.to_dict()
                anomaly_alerts.append(anomaly_alerts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if anomaly_alerts is not UNSET:
            field_dict["anomaly_alerts"] = anomaly_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.anomaly_alert import AnomalyAlert
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        anomaly_alerts = []
        _anomaly_alerts = d.pop("anomaly_alerts", UNSET)
        for anomaly_alerts_item_data in _anomaly_alerts or []:
            anomaly_alerts_item = AnomalyAlert.from_dict(anomaly_alerts_item_data)

            anomaly_alerts.append(anomaly_alerts_item)

        anomaly_alerts = cls(
            links=links,
            anomaly_alerts=anomaly_alerts,
        )

        anomaly_alerts.additional_properties = d
        return anomaly_alerts

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
