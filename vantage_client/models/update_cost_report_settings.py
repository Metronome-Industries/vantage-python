from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCostReportSettings")


@_attrs_define
class UpdateCostReportSettings:
    """Report settings.

    Attributes:
        include_credits (bool | Unset): Report will include credits.
        include_refunds (bool | Unset): Report will include refunds.
        include_discounts (bool | Unset): Report will include discounts.
        include_tax (bool | Unset): Report will include tax.
        amortize (bool | Unset): Report will amortize.
        unallocated (bool | Unset): Report will show unallocated costs.
        aggregate_by (str | Unset): Report will aggregate by cost or usage.
        show_previous_period (bool | Unset): Report will show previous period costs or usage comparison.
    """

    include_credits: bool | Unset = UNSET
    include_refunds: bool | Unset = UNSET
    include_discounts: bool | Unset = UNSET
    include_tax: bool | Unset = UNSET
    amortize: bool | Unset = UNSET
    unallocated: bool | Unset = UNSET
    aggregate_by: str | Unset = UNSET
    show_previous_period: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_credits = self.include_credits

        include_refunds = self.include_refunds

        include_discounts = self.include_discounts

        include_tax = self.include_tax

        amortize = self.amortize

        unallocated = self.unallocated

        aggregate_by = self.aggregate_by

        show_previous_period = self.show_previous_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_credits is not UNSET:
            field_dict["include_credits"] = include_credits
        if include_refunds is not UNSET:
            field_dict["include_refunds"] = include_refunds
        if include_discounts is not UNSET:
            field_dict["include_discounts"] = include_discounts
        if include_tax is not UNSET:
            field_dict["include_tax"] = include_tax
        if amortize is not UNSET:
            field_dict["amortize"] = amortize
        if unallocated is not UNSET:
            field_dict["unallocated"] = unallocated
        if aggregate_by is not UNSET:
            field_dict["aggregate_by"] = aggregate_by
        if show_previous_period is not UNSET:
            field_dict["show_previous_period"] = show_previous_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_credits = d.pop("include_credits", UNSET)

        include_refunds = d.pop("include_refunds", UNSET)

        include_discounts = d.pop("include_discounts", UNSET)

        include_tax = d.pop("include_tax", UNSET)

        amortize = d.pop("amortize", UNSET)

        unallocated = d.pop("unallocated", UNSET)

        aggregate_by = d.pop("aggregate_by", UNSET)

        show_previous_period = d.pop("show_previous_period", UNSET)

        update_cost_report_settings = cls(
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_discounts=include_discounts,
            include_tax=include_tax,
            amortize=amortize,
            unallocated=unallocated,
            aggregate_by=aggregate_by,
            show_previous_period=show_previous_period,
        )

        update_cost_report_settings.additional_properties = d
        return update_cost_report_settings

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
