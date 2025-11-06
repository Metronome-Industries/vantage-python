from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCostAlert")


@_attrs_define
class UpdateCostAlert:
    """Update a Cost Alert

    Attributes:
        title (str | Unset): The title of the Cost Alert.
        email_recipients (list[str] | Unset): The email recipients for the Cost Alert.
        interval (str | Unset): The period of time used to compare costs. Options are 'day', 'week', 'month', 'quarter'.
        threshold (float | Unset): The threshold value for the Cost Alert.
        slack_channels (list[str] | Unset): The Slack channels that will receive the alert. Make sure your slack
            integration is connected at https://console.vantage.sh/settings/slack.
        teams_channels (list[str] | Unset): The Microsoft Teams channels that will receive the alert. Make sure your
            teams integration is connected at https://console.vantage.sh/settings/microsoft_teams.
        unit_type (str | Unset): The unit type used to compare costs. Options are 'currency' or 'percentage'.
        report_tokens (list[str] | Unset): The tokens of the reports to alert on.
    """

    title: str | Unset = UNSET
    email_recipients: list[str] | Unset = UNSET
    interval: str | Unset = UNSET
    threshold: float | Unset = UNSET
    slack_channels: list[str] | Unset = UNSET
    teams_channels: list[str] | Unset = UNSET
    unit_type: str | Unset = UNSET
    report_tokens: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        email_recipients: list[str] | Unset = UNSET
        if not isinstance(self.email_recipients, Unset):
            email_recipients = self.email_recipients

        interval = self.interval

        threshold = self.threshold

        slack_channels: list[str] | Unset = UNSET
        if not isinstance(self.slack_channels, Unset):
            slack_channels = self.slack_channels

        teams_channels: list[str] | Unset = UNSET
        if not isinstance(self.teams_channels, Unset):
            teams_channels = self.teams_channels

        unit_type = self.unit_type

        report_tokens: list[str] | Unset = UNSET
        if not isinstance(self.report_tokens, Unset):
            report_tokens = self.report_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if email_recipients is not UNSET:
            field_dict["email_recipients"] = email_recipients
        if interval is not UNSET:
            field_dict["interval"] = interval
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if teams_channels is not UNSET:
            field_dict["teams_channels"] = teams_channels
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if report_tokens is not UNSET:
            field_dict["report_tokens"] = report_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        email_recipients = cast(list[str], d.pop("email_recipients", UNSET))

        interval = d.pop("interval", UNSET)

        threshold = d.pop("threshold", UNSET)

        slack_channels = cast(list[str], d.pop("slack_channels", UNSET))

        teams_channels = cast(list[str], d.pop("teams_channels", UNSET))

        unit_type = d.pop("unit_type", UNSET)

        report_tokens = cast(list[str], d.pop("report_tokens", UNSET))

        update_cost_alert = cls(
            title=title,
            email_recipients=email_recipients,
            interval=interval,
            threshold=threshold,
            slack_channels=slack_channels,
            teams_channels=teams_channels,
            unit_type=unit_type,
            report_tokens=report_tokens,
        )

        update_cost_alert.additional_properties = d
        return update_cost_alert

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
