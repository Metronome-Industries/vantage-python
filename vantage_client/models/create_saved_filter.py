from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavedFilter")


@_attrs_define
class CreateSavedFilter:
    """Create a SavedFilter for CostReports.

    Attributes:
        title (str): The title of the SavedFilter.
        workspace_token (Union[Unset, str]): The Workspace to associate the SavedFilter with. Required if the API token
            is associated with multiple Workspaces.
        filter_ (Union[Unset, str]): The filter query language to apply to the SavedFilter, which subsequently gets
            applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    """

    title: str
    workspace_token: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        workspace_token = self.workspace_token

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        workspace_token = d.pop("workspace_token", UNSET)

        filter_ = d.pop("filter", UNSET)

        create_saved_filter = cls(
            title=title,
            workspace_token=workspace_token,
            filter_=filter_,
        )

        create_saved_filter.additional_properties = d
        return create_saved_filter

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
