from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalyNotification")


@_attrs_define
class AnomalyNotification:
    """AnomalyNotification model

    Attributes:
        token (Union[Unset, str]):
        cost_report_token (Union[Unset, str]): The token for the CostReport the AnomalyNotification is associated with.
        created_at (Union[Unset, str]): The date and time, in UTC, the AnomalyNotification was created. ISO 8601
            Formatted. Example: 2023-08-04 00:00:00+00:00.
        updated_at (Union[Unset, str]): The date and time, in UTC, the AnomalyNotification was last updated at. ISO 8601
            Formatted. Example: 2023-08-04 00:00:00+00:00.
        threshold (Union[Unset, int]): The threshold amount that must be met for the notification to fire.
        user_tokens (Union[Unset, list[str]]): The tokens of the users that receive the notification.
        recipient_channels (Union[Unset, list[str]]): The channels that the notification is sent to.
    """

    token: Union[Unset, str] = UNSET
    cost_report_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    threshold: Union[Unset, int] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        cost_report_token = self.cost_report_token

        created_at = self.created_at

        updated_at = self.updated_at

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
        if token is not UNSET:
            field_dict["token"] = token
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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
        token = d.pop("token", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        threshold = d.pop("threshold", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        anomaly_notification = cls(
            token=token,
            cost_report_token=cost_report_token,
            created_at=created_at,
            updated_at=updated_at,
            threshold=threshold,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )

        anomaly_notification.additional_properties = d
        return anomaly_notification

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
