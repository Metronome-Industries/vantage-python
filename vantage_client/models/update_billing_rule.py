from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillingRule")


@_attrs_define
class UpdateBillingRule:
    """Update a BillingRule.

    Attributes:
        title (str | Unset): The title of the BillingRule.
        charge_type (str | Unset): The charge type of the BillingRule.
        percentage (float | Unset): The percentage of the cost shown. Example value: 75.0
        service (str | Unset): The service of the BillingRule.
        category (str | Unset): The category of the BillingRule.
        sub_category (str | Unset): The subcategory of the BillingRule.
        start_period (str | Unset): The start period of the BillingRule.
        amount (float | Unset): The credit amount for the BillingRule. Example value: 300
        start_date (str | Unset): The start date of the BillingRule. ISO 8601 formatted.
        end_date (str | Unset): The end date of the BillingRule. ISO 8601 formatted.
        apply_to_all (bool | Unset): Determines if the BillingRule applies to all current and future managed accounts.
        sql_query (str | Unset): The SQL query of the BillingRule.
    """

    title: str | Unset = UNSET
    charge_type: str | Unset = UNSET
    percentage: float | Unset = UNSET
    service: str | Unset = UNSET
    category: str | Unset = UNSET
    sub_category: str | Unset = UNSET
    start_period: str | Unset = UNSET
    amount: float | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    apply_to_all: bool | Unset = UNSET
    sql_query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        charge_type = self.charge_type

        percentage = self.percentage

        service = self.service

        category = self.category

        sub_category = self.sub_category

        start_period = self.start_period

        amount = self.amount

        start_date = self.start_date

        end_date = self.end_date

        apply_to_all = self.apply_to_all

        sql_query = self.sql_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if charge_type is not UNSET:
            field_dict["charge_type"] = charge_type
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if service is not UNSET:
            field_dict["service"] = service
        if category is not UNSET:
            field_dict["category"] = category
        if sub_category is not UNSET:
            field_dict["sub_category"] = sub_category
        if start_period is not UNSET:
            field_dict["start_period"] = start_period
        if amount is not UNSET:
            field_dict["amount"] = amount
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if apply_to_all is not UNSET:
            field_dict["apply_to_all"] = apply_to_all
        if sql_query is not UNSET:
            field_dict["sql_query"] = sql_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        charge_type = d.pop("charge_type", UNSET)

        percentage = d.pop("percentage", UNSET)

        service = d.pop("service", UNSET)

        category = d.pop("category", UNSET)

        sub_category = d.pop("sub_category", UNSET)

        start_period = d.pop("start_period", UNSET)

        amount = d.pop("amount", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        apply_to_all = d.pop("apply_to_all", UNSET)

        sql_query = d.pop("sql_query", UNSET)

        update_billing_rule = cls(
            title=title,
            charge_type=charge_type,
            percentage=percentage,
            service=service,
            category=category,
            sub_category=sub_category,
            start_period=start_period,
            amount=amount,
            start_date=start_date,
            end_date=end_date,
            apply_to_all=apply_to_all,
            sql_query=sql_query,
        )

        update_billing_rule.additional_properties = d
        return update_billing_rule

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
