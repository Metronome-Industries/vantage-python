from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_information import BillingInformation
    from ..models.business_information import BusinessInformation


T = TypeVar("T", bound="ManagedAccount")


@_attrs_define
class ManagedAccount:
    """ManagedAccount model

    Attributes:
        token (Union[Unset, str]):
        name (Union[Unset, str]):
        contact_email (Union[Unset, str]):
        parent_account_token (Union[Unset, str]): The token for the parent Account.
        access_credential_tokens (Union[Unset, list[str]]): The tokens for the Access Credentials assigned to the
            Managed Account.
        billing_rule_tokens (Union[Unset, list[str]]): The tokens for the Billing Rules assigned to the Managed Account.
        msp_billing_profile_token (Union[Unset, str]): Token of the MSP billing profile used for this managed account
            (MSP invoicing accounts only)
        billing_information_attributes (Union[Unset, BillingInformation]):
        business_information_attributes (Union[Unset, BusinessInformation]):
    """

    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    contact_email: Union[Unset, str] = UNSET
    parent_account_token: Union[Unset, str] = UNSET
    access_credential_tokens: Union[Unset, list[str]] = UNSET
    billing_rule_tokens: Union[Unset, list[str]] = UNSET
    msp_billing_profile_token: Union[Unset, str] = UNSET
    billing_information_attributes: Union[Unset, "BillingInformation"] = UNSET
    business_information_attributes: Union[Unset, "BusinessInformation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        contact_email = self.contact_email

        parent_account_token = self.parent_account_token

        access_credential_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.access_credential_tokens, Unset):
            access_credential_tokens = self.access_credential_tokens

        billing_rule_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_rule_tokens, Unset):
            billing_rule_tokens = self.billing_rule_tokens

        msp_billing_profile_token = self.msp_billing_profile_token

        billing_information_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_information_attributes, Unset):
            billing_information_attributes = self.billing_information_attributes.to_dict()

        business_information_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business_information_attributes, Unset):
            business_information_attributes = self.business_information_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if parent_account_token is not UNSET:
            field_dict["parent_account_token"] = parent_account_token
        if access_credential_tokens is not UNSET:
            field_dict["access_credential_tokens"] = access_credential_tokens
        if billing_rule_tokens is not UNSET:
            field_dict["billing_rule_tokens"] = billing_rule_tokens
        if msp_billing_profile_token is not UNSET:
            field_dict["msp_billing_profile_token"] = msp_billing_profile_token
        if billing_information_attributes is not UNSET:
            field_dict["billing_information_attributes"] = billing_information_attributes
        if business_information_attributes is not UNSET:
            field_dict["business_information_attributes"] = business_information_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_information import BillingInformation
        from ..models.business_information import BusinessInformation

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        contact_email = d.pop("contact_email", UNSET)

        parent_account_token = d.pop("parent_account_token", UNSET)

        access_credential_tokens = cast(list[str], d.pop("access_credential_tokens", UNSET))

        billing_rule_tokens = cast(list[str], d.pop("billing_rule_tokens", UNSET))

        msp_billing_profile_token = d.pop("msp_billing_profile_token", UNSET)

        _billing_information_attributes = d.pop("billing_information_attributes", UNSET)
        billing_information_attributes: Union[Unset, BillingInformation]
        if isinstance(_billing_information_attributes, Unset):
            billing_information_attributes = UNSET
        else:
            billing_information_attributes = BillingInformation.from_dict(_billing_information_attributes)

        _business_information_attributes = d.pop("business_information_attributes", UNSET)
        business_information_attributes: Union[Unset, BusinessInformation]
        if isinstance(_business_information_attributes, Unset):
            business_information_attributes = UNSET
        else:
            business_information_attributes = BusinessInformation.from_dict(_business_information_attributes)

        managed_account = cls(
            token=token,
            name=name,
            contact_email=contact_email,
            parent_account_token=parent_account_token,
            access_credential_tokens=access_credential_tokens,
            billing_rule_tokens=billing_rule_tokens,
            msp_billing_profile_token=msp_billing_profile_token,
            billing_information_attributes=billing_information_attributes,
            business_information_attributes=business_information_attributes,
        )

        managed_account.additional_properties = d
        return managed_account

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
