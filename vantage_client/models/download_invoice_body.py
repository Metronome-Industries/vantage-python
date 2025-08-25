from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_invoice_body_file_type import DownloadInvoiceBodyFileType

T = TypeVar("T", bound="DownloadInvoiceBody")


@_attrs_define
class DownloadInvoiceBody:
    """
    Attributes:
        file_type (DownloadInvoiceBodyFileType): Type of file to download (pdf or csv)
    """

    file_type: DownloadInvoiceBodyFileType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_type = self.file_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_type": file_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_type = DownloadInvoiceBodyFileType(d.pop("file_type"))

        download_invoice_body = cls(
            file_type=file_type,
        )

        download_invoice_body.additional_properties = d
        return download_invoice_body

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
