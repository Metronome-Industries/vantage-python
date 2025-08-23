from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_managed_account_billing_information_attributes import (
        UpdateManagedAccountBillingInformationAttributes,
    )
    from ..models.update_managed_account_business_information_attributes import (
        UpdateManagedAccountBusinessInformationAttributes,
    )


T = TypeVar("T", bound="UpdateManagedAccount")


@_attrs_define
class UpdateManagedAccount:
    """Update a Managed Account.

    Attributes:
        name (Union[Unset, str]): The name of the Managed Account.
        contact_email (Union[Unset, str]): The contact email address for the Managed Account.
        access_credential_tokens (Union[Unset, list[str]]): Access Credential (aka Integrations) tokens to assign to the
            Managed Account.
        billing_rule_tokens (Union[Unset, list[str]]): Billing Rule tokens to assign to the Managed Account.
        msp_billing_profile_token (Union[Unset, str]): Token of the MSP billing profile to use for this managed account
            (MSP invoicing accounts only).
        billing_information_attributes (Union[Unset, UpdateManagedAccountBillingInformationAttributes]): Billing address
            and contact information (MSP invoicing accounts only)
        business_information_attributes (Union[Unset, UpdateManagedAccountBusinessInformationAttributes]): Business
            information and custom fields (MSP invoicing accounts only)
    """

    name: Union[Unset, str] = UNSET
    contact_email: Union[Unset, str] = UNSET
    access_credential_tokens: Union[Unset, list[str]] = UNSET
    billing_rule_tokens: Union[Unset, list[str]] = UNSET
    msp_billing_profile_token: Union[Unset, str] = UNSET
    billing_information_attributes: Union[Unset, "UpdateManagedAccountBillingInformationAttributes"] = UNSET
    business_information_attributes: Union[Unset, "UpdateManagedAccountBusinessInformationAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contact_email = self.contact_email

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
        if name is not UNSET:
            field_dict["name"] = name
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
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
        from ..models.update_managed_account_billing_information_attributes import (
            UpdateManagedAccountBillingInformationAttributes,
        )
        from ..models.update_managed_account_business_information_attributes import (
            UpdateManagedAccountBusinessInformationAttributes,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        contact_email = d.pop("contact_email", UNSET)

        access_credential_tokens = cast(list[str], d.pop("access_credential_tokens", UNSET))

        billing_rule_tokens = cast(list[str], d.pop("billing_rule_tokens", UNSET))

        msp_billing_profile_token = d.pop("msp_billing_profile_token", UNSET)

        _billing_information_attributes = d.pop("billing_information_attributes", UNSET)
        billing_information_attributes: Union[Unset, UpdateManagedAccountBillingInformationAttributes]
        if isinstance(_billing_information_attributes, Unset):
            billing_information_attributes = UNSET
        else:
            billing_information_attributes = UpdateManagedAccountBillingInformationAttributes.from_dict(
                _billing_information_attributes
            )

        _business_information_attributes = d.pop("business_information_attributes", UNSET)
        business_information_attributes: Union[Unset, UpdateManagedAccountBusinessInformationAttributes]
        if isinstance(_business_information_attributes, Unset):
            business_information_attributes = UNSET
        else:
            business_information_attributes = UpdateManagedAccountBusinessInformationAttributes.from_dict(
                _business_information_attributes
            )

        update_managed_account = cls(
            name=name,
            contact_email=contact_email,
            access_credential_tokens=access_credential_tokens,
            billing_rule_tokens=billing_rule_tokens,
            msp_billing_profile_token=msp_billing_profile_token,
            billing_information_attributes=billing_information_attributes,
            business_information_attributes=business_information_attributes,
        )

        update_managed_account.additional_properties = d
        return update_managed_account

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
