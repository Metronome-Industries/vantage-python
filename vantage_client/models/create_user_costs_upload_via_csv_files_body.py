from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="CreateUserCostsUploadViaCsvFilesBody")


@_attrs_define
class CreateUserCostsUploadViaCsvFilesBody:
    """
    Attributes:
        csv (File): CSV file containing custom costs
    """

    csv: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csv = self.csv.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "csv": csv,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        csv = self.csv.to_tuple()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "csv": csv,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        csv = File(payload=BytesIO(d.pop("csv")))

        create_user_costs_upload_via_csv_files_body = cls(
            csv=csv,
        )

        create_user_costs_upload_via_csv_files_body.additional_properties = d
        return create_user_costs_upload_via_csv_files_body

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
