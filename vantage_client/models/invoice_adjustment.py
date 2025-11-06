from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adjustment_item import AdjustmentItem


T = TypeVar("T", bound="InvoiceAdjustment")


@_attrs_define
class InvoiceAdjustment:
    """
    Attributes:
        token (str | Unset):
        adjustment_items (AdjustmentItem | Unset):
    """

    token: str | Unset = UNSET
    adjustment_items: AdjustmentItem | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        adjustment_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adjustment_items, Unset):
            adjustment_items = self.adjustment_items.to_dict()

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
        from ..models.adjustment_item import AdjustmentItem

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        _adjustment_items = d.pop("adjustment_items", UNSET)
        adjustment_items: AdjustmentItem | Unset
        if isinstance(_adjustment_items, Unset):
            adjustment_items = UNSET
        else:
            adjustment_items = AdjustmentItem.from_dict(_adjustment_items)

        invoice_adjustment = cls(
            token=token,
            adjustment_items=adjustment_items,
        )

        invoice_adjustment.additional_properties = d
        return invoice_adjustment

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
