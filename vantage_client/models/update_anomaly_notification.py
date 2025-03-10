from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAnomalyNotification")


@_attrs_define
class UpdateAnomalyNotification:
    """Update an Anomaly Notification.

    Attributes:
        threshold (Union[Unset, int]): The threshold amount that must be met for the notification to fire.
        user_tokens (Union[Unset, list[str]]): The tokens of the users that receive the notification.
        recipient_channels (Union[Unset, list[str]]): The Slack/MS Teams channels that receive the notification.
    """

    threshold: Union[Unset, int] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        recipient_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        threshold = d.pop("threshold", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        update_anomaly_notification = cls(
            threshold=threshold,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )

        update_anomaly_notification.additional_properties = d
        return update_anomaly_notification

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
