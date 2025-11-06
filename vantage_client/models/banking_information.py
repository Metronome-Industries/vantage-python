from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.banking_information_secure_data import BankingInformationSecureData


T = TypeVar("T", bound="BankingInformation")


@_attrs_define
class BankingInformation:
    """
    Attributes:
        token (str | Unset):
        bank_name (str | Unset): Name of the bank
        beneficiary_name (str | Unset): Name of the account beneficiary
        tax_id (str | Unset): Tax identification number
        secure_data (BankingInformationSecureData | Unset):
    """

    token: str | Unset = UNSET
    bank_name: str | Unset = UNSET
    beneficiary_name: str | Unset = UNSET
    tax_id: str | Unset = UNSET
    secure_data: BankingInformationSecureData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        bank_name = self.bank_name

        beneficiary_name = self.beneficiary_name

        tax_id = self.tax_id

        secure_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_data, Unset):
            secure_data = self.secure_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if beneficiary_name is not UNSET:
            field_dict["beneficiary_name"] = beneficiary_name
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if secure_data is not UNSET:
            field_dict["secure_data"] = secure_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banking_information_secure_data import BankingInformationSecureData

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        beneficiary_name = d.pop("beneficiary_name", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        _secure_data = d.pop("secure_data", UNSET)
        secure_data: BankingInformationSecureData | Unset
        if isinstance(_secure_data, Unset):
            secure_data = UNSET
        else:
            secure_data = BankingInformationSecureData.from_dict(_secure_data)

        banking_information = cls(
            token=token,
            bank_name=bank_name,
            beneficiary_name=beneficiary_name,
            tax_id=tax_id,
            secure_data=secure_data,
        )

        banking_information.additional_properties = d
        return banking_information

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
