from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Folder")


@_attrs_define
class Folder:
    """Folder model

    Attributes:
        token (str | Unset):
        title (str | Unset): The title of the Folder. Example: Platform Team Reports.
        parent_folder_token (str | Unset): The token for the parent Folder, if any.
        saved_filter_tokens (list[str] | Unset): The tokens for the SavedFilters assigned to the Folder.
        created_at (str | Unset): The date and time, in UTC, the Folder was created. ISO 8601 Formatted. Example:
            2023-08-04T00:00:00Z.
        updated_at (str | Unset): The date and time, in UTC, the Folder was last updated at. ISO 8601 Formatted.
            Example: 2023-08-04T00:00:00Z.
        workspace_token (str | Unset): The token for the Workspace the Folder is a part of.
    """

    token: str | Unset = UNSET
    title: str | Unset = UNSET
    parent_folder_token: str | Unset = UNSET
    saved_filter_tokens: list[str] | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workspace_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        parent_folder_token = self.parent_folder_token

        saved_filter_tokens: list[str] | Unset = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        created_at = self.created_at

        updated_at = self.updated_at

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if parent_folder_token is not UNSET:
            field_dict["parent_folder_token"] = parent_folder_token
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        parent_folder_token = d.pop("parent_folder_token", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        folder = cls(
            token=token,
            title=title,
            parent_folder_token=parent_folder_token,
            saved_filter_tokens=saved_filter_tokens,
            created_at=created_at,
            updated_at=updated_at,
            workspace_token=workspace_token,
        )

        folder.additional_properties = d
        return folder

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
