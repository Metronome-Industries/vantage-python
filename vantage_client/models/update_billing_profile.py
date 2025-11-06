from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_billing_profile_banking_information_attributes import (
        UpdateBillingProfileBankingInformationAttributes,
    )
    from ..models.update_billing_profile_billing_information_attributes import (
        UpdateBillingProfileBillingInformationAttributes,
    )
    from ..models.update_billing_profile_business_information_attributes import (
        UpdateBillingProfileBusinessInformationAttributes,
    )
    from ..models.update_billing_profile_invoice_adjustment_attributes import (
        UpdateBillingProfileInvoiceAdjustmentAttributes,
    )


T = TypeVar("T", bound="UpdateBillingProfile")


@_attrs_define
class UpdateBillingProfile:
    """Update a billing profile (MSP invoicing required).

    Attributes:
        nickname (str | Unset): Display name for the billing profile
        billing_information_attributes (UpdateBillingProfileBillingInformationAttributes | Unset): Billing address and
            contact information
        business_information_attributes (UpdateBillingProfileBusinessInformationAttributes | Unset): Business
            information and custom fields
        banking_information_attributes (UpdateBillingProfileBankingInformationAttributes | Unset): Banking details (MSP
            accounts only)
        invoice_adjustment_attributes (UpdateBillingProfileInvoiceAdjustmentAttributes | Unset): Invoice adjustments
            (taxes, fees, etc.)
    """

    nickname: str | Unset = UNSET
    billing_information_attributes: UpdateBillingProfileBillingInformationAttributes | Unset = UNSET
    business_information_attributes: UpdateBillingProfileBusinessInformationAttributes | Unset = UNSET
    banking_information_attributes: UpdateBillingProfileBankingInformationAttributes | Unset = UNSET
    invoice_adjustment_attributes: UpdateBillingProfileInvoiceAdjustmentAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nickname = self.nickname

        billing_information_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_information_attributes, Unset):
            billing_information_attributes = self.billing_information_attributes.to_dict()

        business_information_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_information_attributes, Unset):
            business_information_attributes = self.business_information_attributes.to_dict()

        banking_information_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.banking_information_attributes, Unset):
            banking_information_attributes = self.banking_information_attributes.to_dict()

        invoice_adjustment_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invoice_adjustment_attributes, Unset):
            invoice_adjustment_attributes = self.invoice_adjustment_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if billing_information_attributes is not UNSET:
            field_dict["billing_information_attributes"] = billing_information_attributes
        if business_information_attributes is not UNSET:
            field_dict["business_information_attributes"] = business_information_attributes
        if banking_information_attributes is not UNSET:
            field_dict["banking_information_attributes"] = banking_information_attributes
        if invoice_adjustment_attributes is not UNSET:
            field_dict["invoice_adjustment_attributes"] = invoice_adjustment_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_billing_profile_banking_information_attributes import (
            UpdateBillingProfileBankingInformationAttributes,
        )
        from ..models.update_billing_profile_billing_information_attributes import (
            UpdateBillingProfileBillingInformationAttributes,
        )
        from ..models.update_billing_profile_business_information_attributes import (
            UpdateBillingProfileBusinessInformationAttributes,
        )
        from ..models.update_billing_profile_invoice_adjustment_attributes import (
            UpdateBillingProfileInvoiceAdjustmentAttributes,
        )

        d = dict(src_dict)
        nickname = d.pop("nickname", UNSET)

        _billing_information_attributes = d.pop("billing_information_attributes", UNSET)
        billing_information_attributes: UpdateBillingProfileBillingInformationAttributes | Unset
        if isinstance(_billing_information_attributes, Unset):
            billing_information_attributes = UNSET
        else:
            billing_information_attributes = UpdateBillingProfileBillingInformationAttributes.from_dict(
                _billing_information_attributes
            )

        _business_information_attributes = d.pop("business_information_attributes", UNSET)
        business_information_attributes: UpdateBillingProfileBusinessInformationAttributes | Unset
        if isinstance(_business_information_attributes, Unset):
            business_information_attributes = UNSET
        else:
            business_information_attributes = UpdateBillingProfileBusinessInformationAttributes.from_dict(
                _business_information_attributes
            )

        _banking_information_attributes = d.pop("banking_information_attributes", UNSET)
        banking_information_attributes: UpdateBillingProfileBankingInformationAttributes | Unset
        if isinstance(_banking_information_attributes, Unset):
            banking_information_attributes = UNSET
        else:
            banking_information_attributes = UpdateBillingProfileBankingInformationAttributes.from_dict(
                _banking_information_attributes
            )

        _invoice_adjustment_attributes = d.pop("invoice_adjustment_attributes", UNSET)
        invoice_adjustment_attributes: UpdateBillingProfileInvoiceAdjustmentAttributes | Unset
        if isinstance(_invoice_adjustment_attributes, Unset):
            invoice_adjustment_attributes = UNSET
        else:
            invoice_adjustment_attributes = UpdateBillingProfileInvoiceAdjustmentAttributes.from_dict(
                _invoice_adjustment_attributes
            )

        update_billing_profile = cls(
            nickname=nickname,
            billing_information_attributes=billing_information_attributes,
            business_information_attributes=business_information_attributes,
            banking_information_attributes=banking_information_attributes,
            invoice_adjustment_attributes=invoice_adjustment_attributes,
        )

        update_billing_profile.additional_properties = d
        return update_billing_profile

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
