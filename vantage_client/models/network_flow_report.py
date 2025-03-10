from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkFlowReport")


@_attrs_define
class NetworkFlowReport:
    """NetworkFlowReport model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the NetworkFlowReport. Example: Public Traffic Destinations.
        default (Union[Unset, bool]): Indicates whether the NetworkFlowReport is the default report.
        created_at (Union[Unset, str]): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the NetworkFlowReport is a part of.
        created_by_token (Union[Unset, str]): The token for the User or Team that created this NetworkFlowReport.
        start_date (Union[Unset, str]): The start date for the NetworkFlowReport. Only set for custom date ranges. ISO
            8601 Formatted. Example: 2024-03-01.
        end_date (Union[Unset, str]): The end date for the NetworkFlowReport. Only set for custom date ranges. ISO 8601
            Formatted. Example: 2024-03-20.
        date_interval (Union[Unset, str]): The date range for the NetworkFlowReport. Only present if a custom date range
            is not specified. Example: last_month.
        groupings (Union[Unset, str]): The grouping aggregations applied to the filtered data. Example: cost_type,
            tag:account.
        flow_direction (Union[Unset, str]): The flow weight of the NetworkFlowReport. Possible values: costs, bytes.
            Example: ingress.
        flow_weight (Union[Unset, str]): The flow weight of the NetworkFlowReport. Possible values: costs, bytes.
            Example: costs.
        filter_ (Union[Unset, str]): The filter applied to the NetworkFlowReport. Additional documentation available at
            https://docs.vantage.sh/vql.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    date_interval: Union[Unset, str] = UNSET
    groupings: Union[Unset, str] = UNSET
    flow_direction: Union[Unset, str] = UNSET
    flow_weight: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        default = self.default

        created_at = self.created_at

        workspace_token = self.workspace_token

        created_by_token = self.created_by_token

        start_date = self.start_date

        end_date = self.end_date

        date_interval = self.date_interval

        groupings = self.groupings

        flow_direction = self.flow_direction

        flow_weight = self.flow_weight

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if default is not UNSET:
            field_dict["default"] = default
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if flow_direction is not UNSET:
            field_dict["flow_direction"] = flow_direction
        if flow_weight is not UNSET:
            field_dict["flow_weight"] = flow_weight
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        default = d.pop("default", UNSET)

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        date_interval = d.pop("date_interval", UNSET)

        groupings = d.pop("groupings", UNSET)

        flow_direction = d.pop("flow_direction", UNSET)

        flow_weight = d.pop("flow_weight", UNSET)

        filter_ = d.pop("filter", UNSET)

        network_flow_report = cls(
            token=token,
            title=title,
            default=default,
            created_at=created_at,
            workspace_token=workspace_token,
            created_by_token=created_by_token,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            groupings=groupings,
            flow_direction=flow_direction,
            flow_weight=flow_weight,
            filter_=filter_,
        )

        network_flow_report.additional_properties = d
        return network_flow_report

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
