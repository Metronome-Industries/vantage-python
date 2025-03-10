from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBudgetAlertJsonBody")


@_attrs_define
class UpdateBudgetAlertJsonBody:
    """
    Attributes:
        budget_tokens (Union[Unset, list[str]]): The tokens of the Budget that has the alert.
        threshold (Union[Unset, int]): The threshold amount that must be met for the alert to fire.
        user_tokens (Union[Unset, list[str]]): The tokens of the users that receive the alert.
        duration_in_days (Union[Unset, int]): The number of days from the start or end of the month to trigger the alert
            if the threshold is reached. For the full month, pass an empty value.
        period_to_track (Union[Unset, str]): The period tracked on the alert. Used with duration_in_days to determine
            the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month,
            end_of_the_month.
        recipient_channels (Union[Unset, list[str]]): The channels receiving the alerts. Requires an integration
            provider to be connected.
    """

    budget_tokens: Union[Unset, list[str]] = UNSET
    threshold: Union[Unset, int] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    duration_in_days: Union[Unset, int] = UNSET
    period_to_track: Union[Unset, str] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.budget_tokens, Unset):
            budget_tokens = self.budget_tokens

        threshold = self.threshold

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        duration_in_days = self.duration_in_days

        period_to_track = self.period_to_track

        recipient_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget_tokens is not UNSET:
            field_dict["budget_tokens"] = budget_tokens
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if duration_in_days is not UNSET:
            field_dict["duration_in_days"] = duration_in_days
        if period_to_track is not UNSET:
            field_dict["period_to_track"] = period_to_track
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        budget_tokens = cast(list[str], d.pop("budget_tokens", UNSET))

        threshold = d.pop("threshold", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        duration_in_days = d.pop("duration_in_days", UNSET)

        period_to_track = d.pop("period_to_track", UNSET)

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        update_budget_alert_json_body = cls(
            budget_tokens=budget_tokens,
            threshold=threshold,
            user_tokens=user_tokens,
            duration_in_days=duration_in_days,
            period_to_track=period_to_track,
            recipient_channels=recipient_channels,
        )

        update_budget_alert_json_body.additional_properties = d
        return update_budget_alert_json_body

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
