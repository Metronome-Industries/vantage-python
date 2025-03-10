from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceReport")


@_attrs_define
class ResourceReport:
    """ResourceReport model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the ResourceReport. Example: Acme123 Active Resources.
        filter_ (Union[Unset, str]): The filter applied to the ResourceReport. Additional documentation available at
            https://docs.vantage.sh/vql.
        created_at (Union[Unset, str]): The date and time, in UTC, the report was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the ResourceReport is a part of.
        user_token (Union[Unset, str]): The token for the User who created this ResourceReport.
        created_by_token (Union[Unset, str]): The token for the User or Team who created this ResourceReport.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    user_token: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        filter_ = self.filter_

        created_at = self.created_at

        workspace_token = self.workspace_token

        user_token = self.user_token

        created_by_token = self.created_by_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if user_token is not UNSET:
            field_dict["user_token"] = user_token
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        filter_ = d.pop("filter", UNSET)

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        user_token = d.pop("user_token", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        resource_report = cls(
            token=token,
            title=title,
            filter_=filter_,
            created_at=created_at,
            workspace_token=workspace_token,
            user_token=user_token,
            created_by_token=created_by_token,
        )

        resource_report.additional_properties = d
        return resource_report

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
