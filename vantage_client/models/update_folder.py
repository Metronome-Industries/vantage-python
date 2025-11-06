from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFolder")


@_attrs_define
class UpdateFolder:
    """Update a Folder for CostReports.

    Attributes:
        title (str | Unset): The title of the Folder.
        parent_folder_token (str | Unset): The token of the parent Folder.
        saved_filter_tokens (list[str] | Unset): The tokens of the SavedFilters to apply to any Cost Report contained
            within the Folder.
    """

    title: str | Unset = UNSET
    parent_folder_token: str | Unset = UNSET
    saved_filter_tokens: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        parent_folder_token = self.parent_folder_token

        saved_filter_tokens: list[str] | Unset = UNSET
        if not isinstance(self.saved_filter_tokens, Unset):
            saved_filter_tokens = self.saved_filter_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if parent_folder_token is not UNSET:
            field_dict["parent_folder_token"] = parent_folder_token
        if saved_filter_tokens is not UNSET:
            field_dict["saved_filter_tokens"] = saved_filter_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        parent_folder_token = d.pop("parent_folder_token", UNSET)

        saved_filter_tokens = cast(list[str], d.pop("saved_filter_tokens", UNSET))

        update_folder = cls(
            title=title,
            parent_folder_token=parent_folder_token,
            saved_filter_tokens=saved_filter_tokens,
        )

        update_folder.additional_properties = d
        return update_folder

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
