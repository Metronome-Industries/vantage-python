from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillingProfileBankingInformationAttributesSecureData")


@_attrs_define
class UpdateBillingProfileBankingInformationAttributesSecureData:
    """Encrypted banking details

    Attributes:
        account_number (str | Unset): Bank account number (US)
        routing_number (str | Unset): Bank routing number (US)
        iban (str | Unset): International Bank Account Number (EU)
        swift_bic (str | Unset): SWIFT/BIC code (EU)
    """

    account_number: str | Unset = UNSET
    routing_number: str | Unset = UNSET
    iban: str | Unset = UNSET
    swift_bic: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        routing_number = self.routing_number

        iban = self.iban

        swift_bic = self.swift_bic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if routing_number is not UNSET:
            field_dict["routing_number"] = routing_number
        if iban is not UNSET:
            field_dict["iban"] = iban
        if swift_bic is not UNSET:
            field_dict["swift_bic"] = swift_bic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        routing_number = d.pop("routing_number", UNSET)

        iban = d.pop("iban", UNSET)

        swift_bic = d.pop("swift_bic", UNSET)

        update_billing_profile_banking_information_attributes_secure_data = cls(
            account_number=account_number,
            routing_number=routing_number,
            iban=iban,
            swift_bic=swift_bic,
        )

        update_billing_profile_banking_information_attributes_secure_data.additional_properties = d
        return update_billing_profile_banking_information_attributes_secure_data

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
