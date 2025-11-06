from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.adjustment_item_adjustment_type import AdjustmentItemAdjustmentType
from ..models.adjustment_item_calculation_type import AdjustmentItemCalculationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdjustmentItem")


@_attrs_define
class AdjustmentItem:
    """
    Attributes:
        name (str | Unset): Name of the adjustment (e.g., 'State Tax', 'Processing Fee')
        adjustment_type (AdjustmentItemAdjustmentType | Unset): Type of adjustment
        calculation_type (AdjustmentItemCalculationType | Unset): How the adjustment is calculated
        amount (str | Unset): Amount or percentage value for the adjustment
    """

    name: str | Unset = UNSET
    adjustment_type: AdjustmentItemAdjustmentType | Unset = UNSET
    calculation_type: AdjustmentItemCalculationType | Unset = UNSET
    amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        adjustment_type: str | Unset = UNSET
        if not isinstance(self.adjustment_type, Unset):
            adjustment_type = self.adjustment_type.value

        calculation_type: str | Unset = UNSET
        if not isinstance(self.calculation_type, Unset):
            calculation_type = self.calculation_type.value

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if adjustment_type is not UNSET:
            field_dict["adjustment_type"] = adjustment_type
        if calculation_type is not UNSET:
            field_dict["calculation_type"] = calculation_type
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _adjustment_type = d.pop("adjustment_type", UNSET)
        adjustment_type: AdjustmentItemAdjustmentType | Unset
        if isinstance(_adjustment_type, Unset):
            adjustment_type = UNSET
        else:
            adjustment_type = AdjustmentItemAdjustmentType(_adjustment_type)

        _calculation_type = d.pop("calculation_type", UNSET)
        calculation_type: AdjustmentItemCalculationType | Unset
        if isinstance(_calculation_type, Unset):
            calculation_type = UNSET
        else:
            calculation_type = AdjustmentItemCalculationType(_calculation_type)

        amount = d.pop("amount", UNSET)

        adjustment_item = cls(
            name=name,
            adjustment_type=adjustment_type,
            calculation_type=calculation_type,
            amount=amount,
        )

        adjustment_item.additional_properties = d
        return adjustment_item

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
