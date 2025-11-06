from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_billing_profile_invoice_adjustment_attributes_adjustment_items_item_adjustment_type import (
    UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType,
)
from ..models.update_billing_profile_invoice_adjustment_attributes_adjustment_items_item_calculation_type import (
    UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem")


@_attrs_define
class UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem:
    """
    Attributes:
        name (str): Name of the adjustment
        calculation_type (UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType): How the
            adjustment is calculated
        amount (float): Amount or percentage value
        adjustment_type (UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType | Unset): Type
            of adjustment Default: UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType.CHARGE.
    """

    name: str
    calculation_type: UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType
    amount: float
    adjustment_type: UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType | Unset = (
        UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType.CHARGE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        calculation_type = self.calculation_type.value

        amount = self.amount

        adjustment_type: str | Unset = UNSET
        if not isinstance(self.adjustment_type, Unset):
            adjustment_type = self.adjustment_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "calculation_type": calculation_type,
                "amount": amount,
            }
        )
        if adjustment_type is not UNSET:
            field_dict["adjustment_type"] = adjustment_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        calculation_type = UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemCalculationType(
            d.pop("calculation_type")
        )

        amount = d.pop("amount")

        _adjustment_type = d.pop("adjustment_type", UNSET)
        adjustment_type: UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType | Unset
        if isinstance(_adjustment_type, Unset):
            adjustment_type = UNSET
        else:
            adjustment_type = UpdateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItemAdjustmentType(
                _adjustment_type
            )

        update_billing_profile_invoice_adjustment_attributes_adjustment_items_item = cls(
            name=name,
            calculation_type=calculation_type,
            amount=amount,
            adjustment_type=adjustment_type,
        )

        update_billing_profile_invoice_adjustment_attributes_adjustment_items_item.additional_properties = d
        return update_billing_profile_invoice_adjustment_attributes_adjustment_items_item

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
