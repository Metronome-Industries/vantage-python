from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCostAlert")


@_attrs_define
class CreateCostAlert:
    """Create a new Cost Alert

    Attributes:
        title (str): The title of the Cost Alert.
        interval (str): The period of time used to compare costs. Options are 'day', 'week', 'month', 'quarter'.
        threshold (float): The threshold value for the Cost Alert.
        unit_type (str): The unit type used to compare costs. Options are 'currency' or 'percentage'.
        workspace_token (str): The token of the Workspace to add the Cost Alert to.
        email_recipients (Union[Unset, list[str]]): The email recipients for the Cost Alert.
        slack_channels (Union[Unset, list[str]]): The Slack channels that will receive the alert.
        teams_channels (Union[Unset, list[str]]): The Microsoft Teams channels that will receive the alert.
        report_tokens (Union[Unset, list[str]]): The tokens of the reports to alert on.
    """

    title: str
    interval: str
    threshold: float
    unit_type: str
    workspace_token: str
    email_recipients: Union[Unset, list[str]] = UNSET
    slack_channels: Union[Unset, list[str]] = UNSET
    teams_channels: Union[Unset, list[str]] = UNSET
    report_tokens: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        interval = self.interval

        threshold = self.threshold

        unit_type = self.unit_type

        workspace_token = self.workspace_token

        email_recipients: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email_recipients, Unset):
            email_recipients = self.email_recipients

        slack_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.slack_channels, Unset):
            slack_channels = self.slack_channels

        teams_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.teams_channels, Unset):
            teams_channels = self.teams_channels

        report_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.report_tokens, Unset):
            report_tokens = self.report_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "interval": interval,
                "threshold": threshold,
                "unit_type": unit_type,
                "workspace_token": workspace_token,
            }
        )
        if email_recipients is not UNSET:
            field_dict["email_recipients"] = email_recipients
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if teams_channels is not UNSET:
            field_dict["teams_channels"] = teams_channels
        if report_tokens is not UNSET:
            field_dict["report_tokens"] = report_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        interval = d.pop("interval")

        threshold = d.pop("threshold")

        unit_type = d.pop("unit_type")

        workspace_token = d.pop("workspace_token")

        email_recipients = cast(list[str], d.pop("email_recipients", UNSET))

        slack_channels = cast(list[str], d.pop("slack_channels", UNSET))

        teams_channels = cast(list[str], d.pop("teams_channels", UNSET))

        report_tokens = cast(list[str], d.pop("report_tokens", UNSET))

        create_cost_alert = cls(
            title=title,
            interval=interval,
            threshold=threshold,
            unit_type=unit_type,
            workspace_token=workspace_token,
            email_recipients=email_recipients,
            slack_channels=slack_channels,
            teams_channels=teams_channels,
            report_tokens=report_tokens,
        )

        create_cost_alert.additional_properties = d
        return create_cost_alert

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
