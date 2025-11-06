from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_export_manifest import DataExportManifest


T = TypeVar("T", bound="DataExport")


@_attrs_define
class DataExport:
    """DataExport model

    Attributes:
        token (str | Unset):  Example: dta_xprt_abcd1234567890.
        status (str | Unset):  Example: pending.
        created_at (str | Unset):  Example: 2025-03-20T12:00:00Z.
        export_type (str | Unset):  Example: cost_report.
        manifest (DataExportManifest | Unset):
        attributes (str | Unset):
    """

    token: str | Unset = UNSET
    status: str | Unset = UNSET
    created_at: str | Unset = UNSET
    export_type: str | Unset = UNSET
    manifest: DataExportManifest | Unset = UNSET
    attributes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        status = self.status

        created_at = self.created_at

        export_type = self.export_type

        manifest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        attributes = self.attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if export_type is not UNSET:
            field_dict["export_type"] = export_type
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_export_manifest import DataExportManifest

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("created_at", UNSET)

        export_type = d.pop("export_type", UNSET)

        _manifest = d.pop("manifest", UNSET)
        manifest: DataExportManifest | Unset
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = DataExportManifest.from_dict(_manifest)

        attributes = d.pop("attributes", UNSET)

        data_export = cls(
            token=token,
            status=status,
            created_at=created_at,
            export_type=export_type,
            manifest=manifest,
            attributes=attributes,
        )

        data_export.additional_properties = d
        return data_export

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
