from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankingInformation")


@_attrs_define
class BankingInformation:
    """
    Attributes:
        id (Union[Unset, str]):
        token (Union[Unset, str]):
        bank_name (Union[Unset, str]): Name of the bank
        beneficiary_name (Union[Unset, str]): Name of the account beneficiary
        tax_id (Union[Unset, str]): Tax identification number
        secure_data (Union[Unset, str]): Encrypted banking details (account numbers, routing info)
    """

    id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    beneficiary_name: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    secure_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        bank_name = self.bank_name

        beneficiary_name = self.beneficiary_name

        tax_id = self.tax_id

        secure_data = self.secure_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        beneficiary_name = d.pop("beneficiary_name", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        secure_data = d.pop("secure_data", UNSET)

        banking_information = cls(
            id=id,
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
