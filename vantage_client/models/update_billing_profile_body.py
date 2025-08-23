from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillingProfileBody")


@_attrs_define
class UpdateBillingProfileBody:
    """
    Attributes:
        nickname (Union[Unset, str]): Display name for the billing profile
        billing_information_attributesid (Union[Unset, int]):
        billing_information_attributestoken (Union[Unset, str]):
        billing_information_attributescompany_name (Union[Unset, str]): Company name for billing
        billing_information_attributescountry_code (Union[Unset, str]): ISO country code
        billing_information_attributesaddress_line_1 (Union[Unset, str]): First line of billing address
        billing_information_attributesaddress_line_2 (Union[Unset, str]): Second line of billing address
        billing_information_attributescity (Union[Unset, str]): City for billing address
        billing_information_attributesstate (Union[Unset, str]): State or province for billing address
        billing_information_attributespostal_code (Union[Unset, str]): Postal or ZIP code
        billing_information_attributesbilling_email (Union[Unset, list[str]]): Array of billing email addresses
        business_information_attributesid (Union[Unset, int]):
        business_information_attributestoken (Union[Unset, str]):
        business_information_attributesmetadatacustom_fieldsname (Union[Unset, list[str]]): Custom field name
        business_information_attributesmetadatacustom_fieldsvalue (Union[Unset, list[str]]): Custom field value
        banking_information_attributesid (Union[Unset, int]):
        banking_information_attributestoken (Union[Unset, str]):
        banking_information_attributesbank_name (Union[Unset, str]): Name of the bank
        banking_information_attributesbeneficiary_name (Union[Unset, str]): Name of the account beneficiary
        banking_information_attributestax_id (Union[Unset, str]): Tax identification number
        banking_information_attributessecure_dataaccount_number (Union[Unset, str]): Bank account number (US)
        banking_information_attributessecure_datarouting_number (Union[Unset, str]): Bank routing number (US)
        banking_information_attributessecure_dataiban (Union[Unset, str]): International Bank Account Number (EU)
        banking_information_attributessecure_dataswift_bic (Union[Unset, str]): SWIFT/BIC code (EU)
    """

    nickname: Union[Unset, str] = UNSET
    billing_information_attributesid: Union[Unset, int] = UNSET
    billing_information_attributestoken: Union[Unset, str] = UNSET
    billing_information_attributescompany_name: Union[Unset, str] = UNSET
    billing_information_attributescountry_code: Union[Unset, str] = UNSET
    billing_information_attributesaddress_line_1: Union[Unset, str] = UNSET
    billing_information_attributesaddress_line_2: Union[Unset, str] = UNSET
    billing_information_attributescity: Union[Unset, str] = UNSET
    billing_information_attributesstate: Union[Unset, str] = UNSET
    billing_information_attributespostal_code: Union[Unset, str] = UNSET
    billing_information_attributesbilling_email: Union[Unset, list[str]] = UNSET
    business_information_attributesid: Union[Unset, int] = UNSET
    business_information_attributestoken: Union[Unset, str] = UNSET
    business_information_attributesmetadatacustom_fieldsname: Union[Unset, list[str]] = UNSET
    business_information_attributesmetadatacustom_fieldsvalue: Union[Unset, list[str]] = UNSET
    banking_information_attributesid: Union[Unset, int] = UNSET
    banking_information_attributestoken: Union[Unset, str] = UNSET
    banking_information_attributesbank_name: Union[Unset, str] = UNSET
    banking_information_attributesbeneficiary_name: Union[Unset, str] = UNSET
    banking_information_attributestax_id: Union[Unset, str] = UNSET
    banking_information_attributessecure_dataaccount_number: Union[Unset, str] = UNSET
    banking_information_attributessecure_datarouting_number: Union[Unset, str] = UNSET
    banking_information_attributessecure_dataiban: Union[Unset, str] = UNSET
    banking_information_attributessecure_dataswift_bic: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nickname = self.nickname

        billing_information_attributesid = self.billing_information_attributesid

        billing_information_attributestoken = self.billing_information_attributestoken

        billing_information_attributescompany_name = self.billing_information_attributescompany_name

        billing_information_attributescountry_code = self.billing_information_attributescountry_code

        billing_information_attributesaddress_line_1 = self.billing_information_attributesaddress_line_1

        billing_information_attributesaddress_line_2 = self.billing_information_attributesaddress_line_2

        billing_information_attributescity = self.billing_information_attributescity

        billing_information_attributesstate = self.billing_information_attributesstate

        billing_information_attributespostal_code = self.billing_information_attributespostal_code

        billing_information_attributesbilling_email: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_information_attributesbilling_email, Unset):
            billing_information_attributesbilling_email = self.billing_information_attributesbilling_email

        business_information_attributesid = self.business_information_attributesid

        business_information_attributestoken = self.business_information_attributestoken

        business_information_attributesmetadatacustom_fieldsname: Union[Unset, list[str]] = UNSET
        if not isinstance(self.business_information_attributesmetadatacustom_fieldsname, Unset):
            business_information_attributesmetadatacustom_fieldsname = (
                self.business_information_attributesmetadatacustom_fieldsname
            )

        business_information_attributesmetadatacustom_fieldsvalue: Union[Unset, list[str]] = UNSET
        if not isinstance(self.business_information_attributesmetadatacustom_fieldsvalue, Unset):
            business_information_attributesmetadatacustom_fieldsvalue = (
                self.business_information_attributesmetadatacustom_fieldsvalue
            )

        banking_information_attributesid = self.banking_information_attributesid

        banking_information_attributestoken = self.banking_information_attributestoken

        banking_information_attributesbank_name = self.banking_information_attributesbank_name

        banking_information_attributesbeneficiary_name = self.banking_information_attributesbeneficiary_name

        banking_information_attributestax_id = self.banking_information_attributestax_id

        banking_information_attributessecure_dataaccount_number = (
            self.banking_information_attributessecure_dataaccount_number
        )

        banking_information_attributessecure_datarouting_number = (
            self.banking_information_attributessecure_datarouting_number
        )

        banking_information_attributessecure_dataiban = self.banking_information_attributessecure_dataiban

        banking_information_attributessecure_dataswift_bic = self.banking_information_attributessecure_dataswift_bic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if billing_information_attributesid is not UNSET:
            field_dict["billing_information_attributes[id]"] = billing_information_attributesid
        if billing_information_attributestoken is not UNSET:
            field_dict["billing_information_attributes[token]"] = billing_information_attributestoken
        if billing_information_attributescompany_name is not UNSET:
            field_dict["billing_information_attributes[company_name]"] = billing_information_attributescompany_name
        if billing_information_attributescountry_code is not UNSET:
            field_dict["billing_information_attributes[country_code]"] = billing_information_attributescountry_code
        if billing_information_attributesaddress_line_1 is not UNSET:
            field_dict["billing_information_attributes[address_line_1]"] = billing_information_attributesaddress_line_1
        if billing_information_attributesaddress_line_2 is not UNSET:
            field_dict["billing_information_attributes[address_line_2]"] = billing_information_attributesaddress_line_2
        if billing_information_attributescity is not UNSET:
            field_dict["billing_information_attributes[city]"] = billing_information_attributescity
        if billing_information_attributesstate is not UNSET:
            field_dict["billing_information_attributes[state]"] = billing_information_attributesstate
        if billing_information_attributespostal_code is not UNSET:
            field_dict["billing_information_attributes[postal_code]"] = billing_information_attributespostal_code
        if billing_information_attributesbilling_email is not UNSET:
            field_dict["billing_information_attributes[billing_email]"] = billing_information_attributesbilling_email
        if business_information_attributesid is not UNSET:
            field_dict["business_information_attributes[id]"] = business_information_attributesid
        if business_information_attributestoken is not UNSET:
            field_dict["business_information_attributes[token]"] = business_information_attributestoken
        if business_information_attributesmetadatacustom_fieldsname is not UNSET:
            field_dict["business_information_attributes[metadata][custom_fields][name]"] = (
                business_information_attributesmetadatacustom_fieldsname
            )
        if business_information_attributesmetadatacustom_fieldsvalue is not UNSET:
            field_dict["business_information_attributes[metadata][custom_fields][value]"] = (
                business_information_attributesmetadatacustom_fieldsvalue
            )
        if banking_information_attributesid is not UNSET:
            field_dict["banking_information_attributes[id]"] = banking_information_attributesid
        if banking_information_attributestoken is not UNSET:
            field_dict["banking_information_attributes[token]"] = banking_information_attributestoken
        if banking_information_attributesbank_name is not UNSET:
            field_dict["banking_information_attributes[bank_name]"] = banking_information_attributesbank_name
        if banking_information_attributesbeneficiary_name is not UNSET:
            field_dict["banking_information_attributes[beneficiary_name]"] = (
                banking_information_attributesbeneficiary_name
            )
        if banking_information_attributestax_id is not UNSET:
            field_dict["banking_information_attributes[tax_id]"] = banking_information_attributestax_id
        if banking_information_attributessecure_dataaccount_number is not UNSET:
            field_dict["banking_information_attributes[secure_data][account_number]"] = (
                banking_information_attributessecure_dataaccount_number
            )
        if banking_information_attributessecure_datarouting_number is not UNSET:
            field_dict["banking_information_attributes[secure_data][routing_number]"] = (
                banking_information_attributessecure_datarouting_number
            )
        if banking_information_attributessecure_dataiban is not UNSET:
            field_dict["banking_information_attributes[secure_data][iban]"] = (
                banking_information_attributessecure_dataiban
            )
        if banking_information_attributessecure_dataswift_bic is not UNSET:
            field_dict["banking_information_attributes[secure_data][swift_bic]"] = (
                banking_information_attributessecure_dataswift_bic
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nickname = d.pop("nickname", UNSET)

        billing_information_attributesid = d.pop("billing_information_attributes[id]", UNSET)

        billing_information_attributestoken = d.pop("billing_information_attributes[token]", UNSET)

        billing_information_attributescompany_name = d.pop("billing_information_attributes[company_name]", UNSET)

        billing_information_attributescountry_code = d.pop("billing_information_attributes[country_code]", UNSET)

        billing_information_attributesaddress_line_1 = d.pop("billing_information_attributes[address_line_1]", UNSET)

        billing_information_attributesaddress_line_2 = d.pop("billing_information_attributes[address_line_2]", UNSET)

        billing_information_attributescity = d.pop("billing_information_attributes[city]", UNSET)

        billing_information_attributesstate = d.pop("billing_information_attributes[state]", UNSET)

        billing_information_attributespostal_code = d.pop("billing_information_attributes[postal_code]", UNSET)

        billing_information_attributesbilling_email = cast(
            list[str], d.pop("billing_information_attributes[billing_email]", UNSET)
        )

        business_information_attributesid = d.pop("business_information_attributes[id]", UNSET)

        business_information_attributestoken = d.pop("business_information_attributes[token]", UNSET)

        business_information_attributesmetadatacustom_fieldsname = cast(
            list[str], d.pop("business_information_attributes[metadata][custom_fields][name]", UNSET)
        )

        business_information_attributesmetadatacustom_fieldsvalue = cast(
            list[str], d.pop("business_information_attributes[metadata][custom_fields][value]", UNSET)
        )

        banking_information_attributesid = d.pop("banking_information_attributes[id]", UNSET)

        banking_information_attributestoken = d.pop("banking_information_attributes[token]", UNSET)

        banking_information_attributesbank_name = d.pop("banking_information_attributes[bank_name]", UNSET)

        banking_information_attributesbeneficiary_name = d.pop(
            "banking_information_attributes[beneficiary_name]", UNSET
        )

        banking_information_attributestax_id = d.pop("banking_information_attributes[tax_id]", UNSET)

        banking_information_attributessecure_dataaccount_number = d.pop(
            "banking_information_attributes[secure_data][account_number]", UNSET
        )

        banking_information_attributessecure_datarouting_number = d.pop(
            "banking_information_attributes[secure_data][routing_number]", UNSET
        )

        banking_information_attributessecure_dataiban = d.pop(
            "banking_information_attributes[secure_data][iban]", UNSET
        )

        banking_information_attributessecure_dataswift_bic = d.pop(
            "banking_information_attributes[secure_data][swift_bic]", UNSET
        )

        update_billing_profile_body = cls(
            nickname=nickname,
            billing_information_attributesid=billing_information_attributesid,
            billing_information_attributestoken=billing_information_attributestoken,
            billing_information_attributescompany_name=billing_information_attributescompany_name,
            billing_information_attributescountry_code=billing_information_attributescountry_code,
            billing_information_attributesaddress_line_1=billing_information_attributesaddress_line_1,
            billing_information_attributesaddress_line_2=billing_information_attributesaddress_line_2,
            billing_information_attributescity=billing_information_attributescity,
            billing_information_attributesstate=billing_information_attributesstate,
            billing_information_attributespostal_code=billing_information_attributespostal_code,
            billing_information_attributesbilling_email=billing_information_attributesbilling_email,
            business_information_attributesid=business_information_attributesid,
            business_information_attributestoken=business_information_attributestoken,
            business_information_attributesmetadatacustom_fieldsname=business_information_attributesmetadatacustom_fieldsname,
            business_information_attributesmetadatacustom_fieldsvalue=business_information_attributesmetadatacustom_fieldsvalue,
            banking_information_attributesid=banking_information_attributesid,
            banking_information_attributestoken=banking_information_attributestoken,
            banking_information_attributesbank_name=banking_information_attributesbank_name,
            banking_information_attributesbeneficiary_name=banking_information_attributesbeneficiary_name,
            banking_information_attributestax_id=banking_information_attributestax_id,
            banking_information_attributessecure_dataaccount_number=banking_information_attributessecure_dataaccount_number,
            banking_information_attributessecure_datarouting_number=banking_information_attributessecure_datarouting_number,
            banking_information_attributessecure_dataiban=banking_information_attributessecure_dataiban,
            banking_information_attributessecure_dataswift_bic=banking_information_attributessecure_dataswift_bic,
        )

        update_billing_profile_body.additional_properties = d
        return update_billing_profile_body

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
