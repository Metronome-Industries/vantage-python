from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateManagedAccountBillingInformationAttributes")


@_attrs_define
class UpdateManagedAccountBillingInformationAttributes:
    """Billing address and contact information (MSP invoicing accounts only)

    Attributes:
        id (Union[Unset, int]):
        token (Union[Unset, str]):
        company_name (Union[Unset, str]): Company name for billing
        country_code (Union[Unset, str]): ISO country code
        address_line_1 (Union[Unset, str]): First line of billing address
        address_line_2 (Union[Unset, str]): Second line of billing address
        city (Union[Unset, str]): City for billing address
        state (Union[Unset, str]): State or province for billing address
        postal_code (Union[Unset, str]): Postal or ZIP code
        billing_email (Union[Unset, list[str]]): Array of billing email addresses
    """

    id: Union[Unset, int] = UNSET
    token: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    billing_email: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        company_name = self.company_name

        country_code = self.country_code

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        city = self.city

        state = self.state

        postal_code = self.postal_code

        billing_email: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_email, Unset):
            billing_email = self.billing_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if address_line_1 is not UNSET:
            field_dict["address_line_1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        company_name = d.pop("company_name", UNSET)

        country_code = d.pop("country_code", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        billing_email = cast(list[str], d.pop("billing_email", UNSET))

        update_managed_account_billing_information_attributes = cls(
            id=id,
            token=token,
            company_name=company_name,
            country_code=country_code,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            postal_code=postal_code,
            billing_email=billing_email,
        )

        update_managed_account_billing_information_attributes.additional_properties = d
        return update_managed_account_billing_information_attributes

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
