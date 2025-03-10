from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetAlert")


@_attrs_define
class BudgetAlert:
    """BudgetAlert model

    Attributes:
        token (Union[Unset, str]):
        budget_tokens (Union[Unset, list[str]]): The tokens for the Budgets that the Budget Alert is monitoring to
            trigger alerts on.
        created_at (Union[Unset, str]): The date and time, in UTC, the Budget Alert was created. ISO 8601 Formatted.
            Example: 2024-03-19 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the ResourceReport is a part of.
        user_token (Union[Unset, str]): The token for the User who created this BudgetAlert.
        user_tokens (Union[Unset, list[str]]): The Users that receive the alert.
        duration_in_days (Union[Unset, str]): The number of days from the start or end of the month to trigger the alert
            if the threshold is reached.
        threshold (Union[Unset, str]): Alerts only send if they reach this number (as a percentage). When threshold is
            100, that means alerts are triggered once costs reach 100% of the budget. Example: 75.
        period_to_track (Union[Unset, str]): The period tracked on the alert. Used with duration_in_days to determine
            the time window of the alert. Possible values: start_of_the_month, end_of_the_month. Example:
            start_of_the_month.
        integration_provider (Union[Unset, str]): The provider used for sending alerts. This must be configured in the
            console. Possible values are: slack, microsoft_graph. Example: slack.
        recipient_channels (Union[Unset, str]): The channels receiving the alerts. Requires an integration provider to
            be connected.
    """

    token: Union[Unset, str] = UNSET
    budget_tokens: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    user_token: Union[Unset, str] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    duration_in_days: Union[Unset, str] = UNSET
    threshold: Union[Unset, str] = UNSET
    period_to_track: Union[Unset, str] = UNSET
    integration_provider: Union[Unset, str] = UNSET
    recipient_channels: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        budget_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.budget_tokens, Unset):
            budget_tokens = self.budget_tokens

        created_at = self.created_at

        workspace_token = self.workspace_token

        user_token = self.user_token

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        duration_in_days = self.duration_in_days

        threshold = self.threshold

        period_to_track = self.period_to_track

        integration_provider = self.integration_provider

        recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if budget_tokens is not UNSET:
            field_dict["budget_tokens"] = budget_tokens
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if user_token is not UNSET:
            field_dict["user_token"] = user_token
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if duration_in_days is not UNSET:
            field_dict["duration_in_days"] = duration_in_days
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if period_to_track is not UNSET:
            field_dict["period_to_track"] = period_to_track
        if integration_provider is not UNSET:
            field_dict["integration_provider"] = integration_provider
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        budget_tokens = cast(list[str], d.pop("budget_tokens", UNSET))

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        user_token = d.pop("user_token", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        duration_in_days = d.pop("duration_in_days", UNSET)

        threshold = d.pop("threshold", UNSET)

        period_to_track = d.pop("period_to_track", UNSET)

        integration_provider = d.pop("integration_provider", UNSET)

        recipient_channels = d.pop("recipient_channels", UNSET)

        budget_alert = cls(
            token=token,
            budget_tokens=budget_tokens,
            created_at=created_at,
            workspace_token=workspace_token,
            user_token=user_token,
            user_tokens=user_tokens,
            duration_in_days=duration_in_days,
            threshold=threshold,
            period_to_track=period_to_track,
            integration_provider=integration_provider,
            recipient_channels=recipient_channels,
        )

        budget_alert.additional_properties = d
        return budget_alert

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
