from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_billing_profile_business_information_attributes_metadata_custom_fields_item import (
        UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem,
    )


T = TypeVar("T", bound="UpdateBillingProfileBusinessInformationAttributesMetadata")


@_attrs_define
class UpdateBillingProfileBusinessInformationAttributesMetadata:
    """Business metadata including custom fields

    Attributes:
        custom_fields (list[UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem] | Unset): Array
            of custom field objects
    """

    custom_fields: list[UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_billing_profile_business_information_attributes_metadata_custom_fields_item import (
            UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem,
        )

        d = dict(src_dict)
        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: list[UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = (
                    UpdateBillingProfileBusinessInformationAttributesMetadataCustomFieldsItem.from_dict(
                        custom_fields_item_data
                    )
                )

                custom_fields.append(custom_fields_item)

        update_billing_profile_business_information_attributes_metadata = cls(
            custom_fields=custom_fields,
        )

        update_billing_profile_business_information_attributes_metadata.additional_properties = d
        return update_billing_profile_business_information_attributes_metadata

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
