from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedFilter")


@_attrs_define
class SavedFilter:
    """SavedFilter model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the SavedFilter. Example: Platform Team Reports.
        cost_report_tokens (Union[Unset, list[str]]): The tokens for any CostReports the SavedFilter is applied to.
        filter_ (Union[Unset, str]): The SavedFilter's filter, applied to any relevant CostReports. Additional
            documentation available at https://docs.vantage.sh/vql. Example: costs.provider = 'azure'.
        created_at (Union[Unset, str]): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2023-08-04 00:00:00+00:00.
        created_by (Union[Unset, str]): The token for the Creator of this SavedFilter.
        workspace_token (Union[Unset, str]): The token for the Workspace the SavedFilter is a part of.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    cost_report_tokens: Union[Unset, list[str]] = UNSET
    filter_: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        cost_report_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cost_report_tokens, Unset):
            cost_report_tokens = self.cost_report_tokens

        filter_ = self.filter_

        created_at = self.created_at

        created_by = self.created_by

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if cost_report_tokens is not UNSET:
            field_dict["cost_report_tokens"] = cost_report_tokens
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        cost_report_tokens = cast(list[str], d.pop("cost_report_tokens", UNSET))

        filter_ = d.pop("filter", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by = d.pop("created_by", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        saved_filter = cls(
            token=token,
            title=title,
            cost_report_tokens=cost_report_tokens,
            filter_=filter_,
            created_at=created_at,
            created_by=created_by,
            workspace_token=workspace_token,
        )

        saved_filter.additional_properties = d
        return saved_filter

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
