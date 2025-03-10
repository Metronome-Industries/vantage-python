from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFolder")


@_attrs_define
class CreateFolder:
    """Create a Folder for CostReports.

    Attributes:
        title (str): The title of the Folder.
        parent_folder_token (Union[Unset, str]): The token of the parent Folder.
        saved_filter_tokens (Union[Unset, list[str]]): The tokens of the SavedFilters to apply to any Cost Report
            contained within the Folder.
        workspace_token (Union[Unset, str]): The token of the Workspace to add the Folder to. Ignored if
            'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.
    """

    title: str
    parent_folder_token: Union[Unset, str] = UNSET
    saved_filter_tokens: Union[Unset, list[str]] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        parent_folder_token = self.parent_folder_token

        saved_filter_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if parent_folder_token is not UNSET:
            field_dict["parent_folder_token"] = parent_folder_token
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        parent_folder_token = d.pop("parent_folder_token", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        workspace_token = d.pop("workspace_token", UNSET)

        create_folder = cls(
            title=title,
            parent_folder_token=parent_folder_token,
            saved_filter_tokens=saved_filter_tokens,
            workspace_token=workspace_token,
        )

        create_folder.additional_properties = d
        return create_folder

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
