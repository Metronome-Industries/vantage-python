from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAnomalyNotification")


@_attrs_define
class CreateAnomalyNotification:
    """Create an Anomaly Notification for a Cost Report.

    Attributes:
        cost_report_token (str): The token of the Cost Report that has the notification.
        threshold (int | Unset): The threshold amount that must be met for the notification to fire.
        user_tokens (list[str] | Unset): The tokens of the Users that receive the notification.
        recipient_channels (list[str] | Unset): The Slack/MS Teams channels that receive the notification.
    """

    cost_report_token: str
    threshold: int | Unset = UNSET
    user_tokens: list[str] | Unset = UNSET
    recipient_channels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_report_token = self.cost_report_token

        threshold = self.threshold

        user_tokens: list[str] | Unset = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        recipient_channels: list[str] | Unset = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_report_token": cost_report_token,
            }
        )
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_report_token = d.pop("cost_report_token")

        threshold = d.pop("threshold", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        create_anomaly_notification = cls(
            cost_report_token=cost_report_token,
            threshold=threshold,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )

        create_anomaly_notification.additional_properties = d
        return create_anomaly_notification

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
