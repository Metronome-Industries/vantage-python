from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateUserCostsUploadViaCsvDataBody")


@_attrs_define
class CreateUserCostsUploadViaCsvDataBody:
    """
    Attributes:
        csv (File): CSV file containing custom costs
        auto_transform (bool | Unset): Attempt to automatically transform the CSV file to match the FOCUS format.
            Default: False.
    """

    csv: File
    auto_transform: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csv = self.csv.to_tuple()

        auto_transform = self.auto_transform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "csv": csv,
            }
        )
        if auto_transform is not UNSET:
            field_dict["auto_transform"] = auto_transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csv = File(payload=BytesIO(d.pop("csv")))

        auto_transform = d.pop("auto_transform", UNSET)

        create_user_costs_upload_via_csv_data_body = cls(
            csv=csv,
            auto_transform=auto_transform,
        )

        create_user_costs_upload_via_csv_data_body.additional_properties = d
        return create_user_costs_upload_via_csv_data_body

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
