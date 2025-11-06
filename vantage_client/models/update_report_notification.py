from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateReportNotification")


@_attrs_define
class UpdateReportNotification:
    """Update a ReportNotification.

    Attributes:
        title (str | Unset): The title of the ReportNotification.
        cost_report_token (str | Unset): The CostReport token.
        user_tokens (list[str] | Unset): The Users that receive the notification.
        recipient_channels (list[str] | Unset): The Slack or Microsoft Teams channels that receive the notification.
        frequency (str | Unset): The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
        change (str | Unset): The type of change the ReportNotification is tracking. Possible values: percentage,
            dollars.
    """

    title: str | Unset = UNSET
    cost_report_token: str | Unset = UNSET
    user_tokens: list[str] | Unset = UNSET
    recipient_channels: list[str] | Unset = UNSET
    frequency: str | Unset = UNSET
    change: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        cost_report_token = self.cost_report_token

        user_tokens: list[str] | Unset = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        recipient_channels: list[str] | Unset = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        frequency = self.frequency

        change = self.change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        frequency = d.pop("frequency", UNSET)

        change = d.pop("change", UNSET)

        update_report_notification = cls(
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )

        update_report_notification.additional_properties = d
        return update_report_notification

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
