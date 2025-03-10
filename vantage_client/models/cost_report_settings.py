from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostReportSettings")


@_attrs_define
class CostReportSettings:
    """Report settings.

    Attributes:
        include_credits (Union[Unset, bool]): Report will include credits. Default: False.
        include_refunds (Union[Unset, bool]): Report will include refunds. Default: False.
        include_discounts (Union[Unset, bool]): Report will include discounts. Default: True.
        include_tax (Union[Unset, bool]): Report will include tax. Default: True.
        amortize (Union[Unset, bool]): Report will amortize. Default: True.
        unallocated (Union[Unset, bool]): Report will show unallocated costs. Default: False.
        aggregate_by (Union[Unset, str]): Report will aggregate by cost or usage. Default: 'cost'.
    """

    include_credits: Union[Unset, bool] = False
    include_refunds: Union[Unset, bool] = False
    include_discounts: Union[Unset, bool] = True
    include_tax: Union[Unset, bool] = True
    amortize: Union[Unset, bool] = True
    unallocated: Union[Unset, bool] = False
    aggregate_by: Union[Unset, str] = "cost"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_credits = self.include_credits

        include_refunds = self.include_refunds

        include_discounts = self.include_discounts

        include_tax = self.include_tax

        amortize = self.amortize

        unallocated = self.unallocated

        aggregate_by = self.aggregate_by

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        include_credits = d.pop("include_credits", UNSET)

        include_refunds = d.pop("include_refunds", UNSET)

        include_discounts = d.pop("include_discounts", UNSET)

        include_tax = d.pop("include_tax", UNSET)

        amortize = d.pop("amortize", UNSET)

        unallocated = d.pop("unallocated", UNSET)

        aggregate_by = d.pop("aggregate_by", UNSET)

        cost_report_settings = cls(
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_discounts=include_discounts,
            include_tax=include_tax,
            amortize=amortize,
            unallocated=unallocated,
            aggregate_by=aggregate_by,
        )

        cost_report_settings.additional_properties = d
        return cost_report_settings

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
