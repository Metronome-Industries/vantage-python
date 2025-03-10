from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_notification_change import ReportNotificationChange
from ..models.report_notification_frequency import ReportNotificationFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportNotification")


@_attrs_define
class ReportNotification:
    """ReportNotification model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the ReportNotification. Example: Acme Report Notification.
        cost_report_token (Union[Unset, str]): The token for a CostReport the ReportNotification is applied to. Example:
            rprt_abcd1234.
        user_tokens (Union[Unset, list[str]]): The Users that receive the notification.
        recipient_channels (Union[Unset, list[str]]): The Slack or Microsoft Teams channels that receive the
            notification.
        frequency (Union[Unset, ReportNotificationFrequency]): The frequency the ReportNotification is sent. Example:
            weekly.
        change (Union[Unset, ReportNotificationChange]): The type of change the ReportNotification is tracking. Example:
            percentage.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    cost_report_token: Union[Unset, str] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    frequency: Union[Unset, ReportNotificationFrequency] = UNSET
    change: Union[Unset, ReportNotificationChange] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        cost_report_token = self.cost_report_token

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        recipient_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        change: Union[Unset, str] = UNSET
        if not isinstance(self.change, Unset):
            change = self.change.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if change is not UNSET:
            field_dict["change"] = change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, ReportNotificationFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = ReportNotificationFrequency(_frequency)

        _change = d.pop("change", UNSET)
        change: Union[Unset, ReportNotificationChange]
        if isinstance(_change, Unset):
            change = UNSET
        else:
            change = ReportNotificationChange(_change)

        report_notification = cls(
            token=token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )

        report_notification.additional_properties = d
        return report_notification

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
