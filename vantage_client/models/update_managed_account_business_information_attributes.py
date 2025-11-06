from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_managed_account_business_information_attributes_metadata import (
        UpdateManagedAccountBusinessInformationAttributesMetadata,
    )


T = TypeVar("T", bound="UpdateManagedAccountBusinessInformationAttributes")


@_attrs_define
class UpdateManagedAccountBusinessInformationAttributes:
    """Business information and custom fields (MSP invoicing accounts only)

    Attributes:
        id (int | Unset):
        token (str | Unset):
        metadata (UpdateManagedAccountBusinessInformationAttributesMetadata | Unset): Business metadata including custom
            fields
    """

    id: int | Unset = UNSET
    token: str | Unset = UNSET
    metadata: UpdateManagedAccountBusinessInformationAttributesMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_managed_account_business_information_attributes_metadata import (
            UpdateManagedAccountBusinessInformationAttributesMetadata,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateManagedAccountBusinessInformationAttributesMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateManagedAccountBusinessInformationAttributesMetadata.from_dict(_metadata)

        update_managed_account_business_information_attributes = cls(
            id=id,
            token=token,
            metadata=metadata,
        )

        update_managed_account_business_information_attributes.additional_properties = d
        return update_managed_account_business_information_attributes

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
