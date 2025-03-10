from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReportNotification")


@_attrs_define
class CreateReportNotification:
    """Create a ReportNotification.

    Attributes:
        title (str): The title of the ReportNotification.
        cost_report_token (str): The CostReport token.
        frequency (str): The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
        change (str): The type of change the ReportNotification is tracking. Possible values: percentage, dollars.
        workspace_token (Union[Unset, str]): The token of the Workspace to add the ReportNotification to. Required if
            the API token is associated with multiple Workspaces.
        user_tokens (Union[Unset, list[str]]): The Users that receive the notification.
        recipient_channels (Union[Unset, list[str]]): The Slack or Microsoft Teams channels that receive the
            notification.
    """

    title: str
    cost_report_token: str
    frequency: str
    change: str
    workspace_token: Union[Unset, str] = UNSET
    user_tokens: Union[Unset, list[str]] = UNSET
    recipient_channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        cost_report_token = self.cost_report_token

        frequency = self.frequency

        change = self.change

        workspace_token = self.workspace_token

        user_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_tokens, Unset):
            user_tokens = self.user_tokens

        recipient_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_channels, Unset):
            recipient_channels = self.recipient_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "cost_report_token": cost_report_token,
                "frequency": frequency,
                "change": change,
            }
        )
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if user_tokens is not UNSET:
            field_dict["user_tokens"] = user_tokens
        if recipient_channels is not UNSET:
            field_dict["recipient_channels"] = recipient_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        cost_report_token = d.pop("cost_report_token")

        frequency = d.pop("frequency")

        change = d.pop("change")

        workspace_token = d.pop("workspace_token", UNSET)

        user_tokens = cast(list[str], d.pop("user_tokens", UNSET))

        recipient_channels = cast(list[str], d.pop("recipient_channels", UNSET))

        create_report_notification = cls(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )

        create_report_notification.additional_properties = d
        return create_report_notification

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
