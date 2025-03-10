from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBudgetAlertJsonBody")


@_attrs_define
class CreateBudgetAlertJsonBody:
    """
    Attributes:
        budget_tokens (list[str]): The tokens of the Budget that has the alert.
        threshold (int): The threshold amount that must be met for the alert to fire.
        duration_in_days (int): The number of days from the start or end of the month to trigger the alert if the
            threshold is reached.  For the full month, pass an empty value.
        user_tokens (Union[Unset, list[str]]): The tokens of the users that receive the alert.
        period_to_track (Union[Unset, str]): The period tracked on the alert. Used with duration_in_days to determine
            the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month,
            end_of_the_month.
        recipient_channels (Union[Unset, list[str]]): The channels receiving the alerts. Requires an integration
            provider to be connected.
    """

    budget_tokens: list[str]
    threshold: int
    duration_in_days: int
    user_tokens: Union[Unset, list[str]] = UNSET
    period_to_track: Union[Unset, str] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_tokens = self.budget_tokens

        threshold = self.threshold

        duration_in_days = self.duration_in_days

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        period_to_track = self.period_to_track

        recipient_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_tokens": budget_tokens,
                "threshold": threshold,
                "duration_in_days": duration_in_days,
            }
        )
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if period_to_track is not UNSET:
            field_dict["period_to_track"] = period_to_track
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        budget_tokens = cast(list[str], d.pop("budget_tokens"))

        threshold = d.pop("threshold")

        duration_in_days = d.pop("duration_in_days")

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        period_to_track = d.pop("period_to_track", UNSET)

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        create_budget_alert_json_body = cls(
            budget_tokens=budget_tokens,
            threshold=threshold,
            duration_in_days=duration_in_days,
            user_tokens=user_tokens,
            period_to_track=period_to_track,
            recipient_channels=recipient_channels,
        )

        create_budget_alert_json_body.additional_properties = d
        return create_budget_alert_json_body

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
