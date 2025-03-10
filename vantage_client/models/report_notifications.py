from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.report_notification import ReportNotification


T = TypeVar("T", bound="ReportNotifications")


@_attrs_define
class ReportNotifications:
    """ReportNotifications model

    Attributes:
        links (Union[Unset, Links]):
        report_notifications (Union[Unset, list['ReportNotification']]):
    """

    links: Union[Unset, "Links"] = UNSET
    report_notifications: Union[Unset, list["ReportNotification"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        report_notifications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.report_notifications, Unset):
            report_notifications = []
            for report_notifications_item_data in self.report_notifications:
                report_notifications_item = report_notifications_item_data.to_dict()
                report_notifications.append(report_notifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if report_notifications is not UNSET:
            field_dict["report_notifications"] = report_notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.report_notification import ReportNotification

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        report_notifications = []
        _report_notifications = d.pop("report_notifications", UNSET)
        for report_notifications_item_data in _report_notifications or []:
            report_notifications_item = ReportNotification.from_dict(report_notifications_item_data)

            report_notifications.append(report_notifications_item)

        report_notifications = cls(
            links=links,
            report_notifications=report_notifications,
        )

        report_notifications.additional_properties = d
        return report_notifications

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
