from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAlert")


@_attrs_define
class CostAlert:
    """CostAlert model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]):
        email_recipients (Union[Unset, list[str]]): The email addresses that will receive the alert.
        slack_channels (Union[Unset, list[str]]): The Slack channels that will receive the alert. Make sure your slack
            integration is connected at https://console.vantage.sh/settings/slack.
        teams_channels (Union[Unset, list[str]]): The Microsoft Teams channels that will receive the alert. Make sure
            your teams integration is connected at https://console.vantage.sh/settings/microsoft_teams.
        created_at (Union[Unset, str]): The date and time, in UTC, for when the alert was created. ISO 8601 Formatted.
            Example: 2023-10-01T12:00:00Z.
        updated_at (Union[Unset, str]): The date and time, in UTC, for when the alert was last updated. ISO 8601
            Formatted. Example: 2023-10-01T12:00:00Z.
        workspace_token (Union[Unset, str]): The ID of the organization that owns the CostAlert.
        interval (Union[Unset, str]): The period of time used to compare costs. Options are 'day', 'week', 'month',
            'quarter'.
        threshold (Union[Unset, float]): The cost change threshold to alert on.
        unit_type (Union[Unset, str]): The unit type used to compare costs. Options are 'currency' or 'percentage'.
        report_tokens (Union[Unset, list[str]]): The tokens of the reports to alert on.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    email_recipients: Union[Unset, list[str]] = UNSET
    slack_channels: Union[Unset, list[str]] = UNSET
    teams_channels: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    interval: Union[Unset, str] = UNSET
    threshold: Union[Unset, float] = UNSET
    unit_type: Union[Unset, str] = UNSET
    report_tokens: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        email_recipients: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email_recipients, Unset):
            email_recipients = self.email_recipients

        slack_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.slack_channels, Unset):
            slack_channels = self.slack_channels

        teams_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.teams_channels, Unset):
            teams_channels = self.teams_channels

        created_at = self.created_at

        updated_at = self.updated_at

        workspace_token = self.workspace_token

        interval = self.interval

        threshold = self.threshold

        unit_type = self.unit_type

        report_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.report_tokens, Unset):
            report_tokens = self.report_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if email_recipients is not UNSET:
            field_dict["email_recipients"] = email_recipients
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if teams_channels is not UNSET:
            field_dict["teams_channels"] = teams_channels
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if interval is not UNSET:
            field_dict["interval"] = interval
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if report_tokens is not UNSET:
            field_dict["report_tokens"] = report_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        email_recipients = cast(list[str], d.pop("email_recipients", UNSET))

        slack_channels = cast(list[str], d.pop("slack_channels", UNSET))

        teams_channels = cast(list[str], d.pop("teams_channels", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        interval = d.pop("interval", UNSET)

        threshold = d.pop("threshold", UNSET)

        unit_type = d.pop("unit_type", UNSET)

        report_tokens = cast(list[str], d.pop("report_tokens", UNSET))

        cost_alert = cls(
            token=token,
            title=title,
            email_recipients=email_recipients,
            slack_channels=slack_channels,
            teams_channels=teams_channels,
            created_at=created_at,
            updated_at=updated_at,
            workspace_token=workspace_token,
            interval=interval,
            threshold=threshold,
            unit_type=unit_type,
            report_tokens=report_tokens,
        )

        cost_alert.additional_properties = d
        return cost_alert

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
