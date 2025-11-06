from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_billing_profile_business_information_attributes_metadata import (
        UpdateBillingProfileBusinessInformationAttributesMetadata,
    )


T = TypeVar("T", bound="UpdateBillingProfileBusinessInformationAttributes")


@_attrs_define
class UpdateBillingProfileBusinessInformationAttributes:
    """Business information and custom fields

    Attributes:
        token (str | Unset):
        metadata (UpdateBillingProfileBusinessInformationAttributesMetadata | Unset): Business metadata including custom
            fields
    """

    token: str | Unset = UNSET
    metadata: UpdateBillingProfileBusinessInformationAttributesMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_billing_profile_business_information_attributes_metadata import (
            UpdateBillingProfileBusinessInformationAttributesMetadata,
        )

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateBillingProfileBusinessInformationAttributesMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateBillingProfileBusinessInformationAttributesMetadata.from_dict(_metadata)

        update_billing_profile_business_information_attributes = cls(
            token=token,
            metadata=metadata,
        )

        update_billing_profile_business_information_attributes.additional_properties = d
        return update_billing_profile_business_information_attributes

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
