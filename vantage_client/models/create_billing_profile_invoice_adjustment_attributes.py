from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_billing_profile_invoice_adjustment_attributes_adjustment_items_item import (
        CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem,
    )


T = TypeVar("T", bound="CreateBillingProfileInvoiceAdjustmentAttributes")


@_attrs_define
class CreateBillingProfileInvoiceAdjustmentAttributes:
    """Invoice adjustments (taxes, fees, etc.)

    Attributes:
        token (str | Unset):
        adjustment_items (list[CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem] | Unset): Array of
            adjustment items
    """

    token: str | Unset = UNSET
    adjustment_items: list[CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        adjustment_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.adjustment_items, Unset):
            adjustment_items = []
            for adjustment_items_item_data in self.adjustment_items:
                adjustment_items_item = adjustment_items_item_data.to_dict()
                adjustment_items.append(adjustment_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if adjustment_items is not UNSET:
            field_dict["adjustment_items"] = adjustment_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_billing_profile_invoice_adjustment_attributes_adjustment_items_item import (
            CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem,
        )

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        _adjustment_items = d.pop("adjustment_items", UNSET)
        adjustment_items: list[CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem] | Unset = UNSET
        if _adjustment_items is not UNSET:
            adjustment_items = []
            for adjustment_items_item_data in _adjustment_items:
                adjustment_items_item = CreateBillingProfileInvoiceAdjustmentAttributesAdjustmentItemsItem.from_dict(
                    adjustment_items_item_data
                )

                adjustment_items.append(adjustment_items_item)

        create_billing_profile_invoice_adjustment_attributes = cls(
            token=token,
            adjustment_items=adjustment_items,
        )

        create_billing_profile_invoice_adjustment_attributes.additional_properties = d
        return create_billing_profile_invoice_adjustment_attributes

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
