from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_cost_links import UnitCostLinks


T = TypeVar("T", bound="UnitCost")


@_attrs_define
class UnitCost:
    """
    Attributes:
        links (UnitCostLinks | Unset):
        business_metric_token (str | Unset): The token of the BusinessMetric for which the unit cost was calculated.
            Example: bsnss_mtrc_1234.
        business_metric_title (str | Unset): The title of the BusinessMetric for which the unit cost was calculated.
            Example: Total Revenue.
        unit_cost_amount (str | Unset): The amount of the unit cost. Example: 4.25.
        business_metric_amount (str | Unset): The amount of the business metric. Example: 0.371.
        scale (float | Unset): The scale of the BusinessMetric's values within a particular CostReport. Example: 1.0.
        date (str | Unset): The date for which the unit cost was calculated. ISO 8601 Formatted. Example:
            2023-09-05+00:00.
    """

    links: UnitCostLinks | Unset = UNSET
    business_metric_token: str | Unset = UNSET
    business_metric_title: str | Unset = UNSET
    unit_cost_amount: str | Unset = UNSET
    business_metric_amount: str | Unset = UNSET
    scale: float | Unset = UNSET
    date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        business_metric_token = self.business_metric_token

        business_metric_title = self.business_metric_title

        unit_cost_amount = self.unit_cost_amount

        business_metric_amount = self.business_metric_amount

        scale = self.scale

        date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if business_metric_token is not UNSET:
            field_dict["business_metric_token"] = business_metric_token
        if business_metric_title is not UNSET:
            field_dict["business_metric_title"] = business_metric_title
        if unit_cost_amount is not UNSET:
            field_dict["unit_cost_amount"] = unit_cost_amount
        if business_metric_amount is not UNSET:
            field_dict["business_metric_amount"] = business_metric_amount
        if scale is not UNSET:
            field_dict["scale"] = scale
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_cost_links import UnitCostLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: UnitCostLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UnitCostLinks.from_dict(_links)

        business_metric_token = d.pop("business_metric_token", UNSET)

        business_metric_title = d.pop("business_metric_title", UNSET)

        unit_cost_amount = d.pop("unit_cost_amount", UNSET)

        business_metric_amount = d.pop("business_metric_amount", UNSET)

        scale = d.pop("scale", UNSET)

        date = d.pop("date", UNSET)

        unit_cost = cls(
            links=links,
            business_metric_token=business_metric_token,
            business_metric_title=business_metric_title,
            unit_cost_amount=unit_cost_amount,
            business_metric_amount=business_metric_amount,
            scale=scale,
            date=date,
        )

        unit_cost.additional_properties = d
        return unit_cost

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
