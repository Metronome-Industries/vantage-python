from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataExportManifest")


@_attrs_define
class DataExportManifest:
    """
    Attributes:
        files (Union[Unset, str]):
        completed_at (Union[Unset, str]):  Example: 2025-03-20T12:00:00Z.
        valid_until (Union[Unset, str]):  Example: 2025-03-20T12:00:00Z.
    """

    files: Union[Unset, str] = UNSET
    completed_at: Union[Unset, str] = UNSET
    valid_until: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = self.files

        completed_at = self.completed_at

        valid_until = self.valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        files = d.pop("files", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        valid_until = d.pop("valid_until", UNSET)

        data_export_manifest = cls(
            files=files,
            completed_at=completed_at,
            valid_until=valid_until,
        )

        data_export_manifest.additional_properties = d
        return data_export_manifest

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
