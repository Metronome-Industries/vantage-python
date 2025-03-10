from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialCommitmentReport")


@_attrs_define
class FinancialCommitmentReport:
    """FinancialCommitmentReport model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the FinancialCommitmentReport. Example: Acme123 Financial Commitment
            Report.
        default (Union[Unset, bool]): Indicates whether the FinancialCommitmentReport is the default report.
        created_at (Union[Unset, str]): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the FinancialCommitmentReport is a part of.
        user_token (Union[Unset, str]): The token for the User who created this FinancialCommitmentReport.
        start_date (Union[Unset, str]): The start date for the FinancialCommitmentReport. Only set for custom date
            ranges. ISO 8601 Formatted. Example: 2024-03-01.
        end_date (Union[Unset, str]): The end date for the FinancialCommitmentReport. Only set for custom date ranges.
            ISO 8601 Formatted. Example: 2024-03-20.
        date_interval (Union[Unset, str]): The date range for the FinancialCommitmentReport. Only present if a custom
            date range is not specified. Example: last_month.
        date_bucket (Union[Unset, str]): How costs are grouped and displayed in the FinancialCommitmentReport. Possible
            values: day, week, month. Example: month.
        groupings (Union[Unset, str]): The grouping aggregations applied to the filtered data. Example: cost_type,
            tag:account.
        on_demand_costs_scope (Union[Unset, str]): The scope for the costs. Possible values: discountable, all. Example:
            discountable.
        filter_ (Union[Unset, str]): The filter applied to the FinancialCommitmentReport. Additional documentation
            available at https://docs.vantage.sh/vql.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    user_token: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    date_interval: Union[Unset, str] = UNSET
    date_bucket: Union[Unset, str] = UNSET
    groupings: Union[Unset, str] = UNSET
    on_demand_costs_scope: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        default = self.default

        created_at = self.created_at

        workspace_token = self.workspace_token

        user_token = self.user_token

        start_date = self.start_date

        end_date = self.end_date

        date_interval = self.date_interval

        date_bucket = self.date_bucket

        groupings = self.groupings

        on_demand_costs_scope = self.on_demand_costs_scope

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
        if user_token is not UNSET:
            field_dict["user_token"] = user_token
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if date_bucket is not UNSET:
            field_dict["date_bucket"] = date_bucket
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if on_demand_costs_scope is not UNSET:
            field_dict["on_demand_costs_scope"] = on_demand_costs_scope
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

        user_token = d.pop("user_token", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        date_interval = d.pop("date_interval", UNSET)

        date_bucket = d.pop("date_bucket", UNSET)

        groupings = d.pop("groupings", UNSET)

        on_demand_costs_scope = d.pop("on_demand_costs_scope", UNSET)

        filter_ = d.pop("filter", UNSET)

        financial_commitment_report = cls(
            token=token,
            title=title,
            default=default,
            created_at=created_at,
            workspace_token=workspace_token,
            user_token=user_token,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            date_bucket=date_bucket,
            groupings=groupings,
            on_demand_costs_scope=on_demand_costs_scope,
            filter_=filter_,
        )

        financial_commitment_report.additional_properties = d
        return financial_commitment_report

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
