from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_billing_rule_type import CreateBillingRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBillingRule")


@_attrs_define
class CreateBillingRule:
    """Create a BillingRule.

    Attributes:
        type_ (CreateBillingRuleType): The type of the BillingRule. Note: the values are case insensitive.
        title (str): The title of the BillingRule.
        start_period (str | Unset): The start period of the BillingRule. DEPRECATED: use start_date instead.
        start_date (str | Unset): The start date of the BillingRule. ISO 8601 formatted.
        end_date (str | Unset): The end date of the BillingRule. ISO 8601 formatted.
        apply_to_all (bool | Unset): Determines if the BillingRule applies to all current and future managed accounts.
        charge_type (str | Unset): The charge type of the BillingRule. Required for Exclusion rules.
        percentage (float | Unset): The percentage of the cost shown. Required for Adjustment rules. Example value: 75.0
        service (str | Unset): The service of the BillingRule. Required for Charge and Credit rules.
        category (str | Unset): The category of the BillingRule. Required for Charge and Credit rules.
        sub_category (str | Unset): The subcategory of the BillingRule. Required for Charge and Credit rules.
        amount (float | Unset): The amount for the BillingRule. Required for Charge and Credit rules. Example value: 300
        sql_query (str | Unset): The SQL query for the BillingRule. Required for Custom rules. Example value: UPDATE
            costs SET costs.amount = costs.amount * 0.95
    """

    type_: CreateBillingRuleType
    title: str
    start_period: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    apply_to_all: bool | Unset = UNSET
    charge_type: str | Unset = UNSET
    percentage: float | Unset = UNSET
    service: str | Unset = UNSET
    category: str | Unset = UNSET
    sub_category: str | Unset = UNSET
    amount: float | Unset = UNSET
    sql_query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        title = self.title

        start_period = self.start_period

        start_date = self.start_date

        end_date = self.end_date

        apply_to_all = self.apply_to_all

        charge_type = self.charge_type

        percentage = self.percentage

        service = self.service

        category = self.category

        sub_category = self.sub_category

        amount = self.amount

        sql_query = self.sql_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
            }
        )
        if start_period is not UNSET:
            field_dict["start_period"] = start_period
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if apply_to_all is not UNSET:
            field_dict["apply_to_all"] = apply_to_all
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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if sql_query is not UNSET:
            field_dict["sql_query"] = sql_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateBillingRuleType(d.pop("type"))

        title = d.pop("title")

        start_period = d.pop("start_period", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        apply_to_all = d.pop("apply_to_all", UNSET)

        charge_type = d.pop("charge_type", UNSET)

        percentage = d.pop("percentage", UNSET)

        service = d.pop("service", UNSET)

        category = d.pop("category", UNSET)

        sub_category = d.pop("sub_category", UNSET)

        amount = d.pop("amount", UNSET)

        sql_query = d.pop("sql_query", UNSET)

        create_billing_rule = cls(
            type_=type_,
            title=title,
            start_period=start_period,
            start_date=start_date,
            end_date=end_date,
            apply_to_all=apply_to_all,
            charge_type=charge_type,
            percentage=percentage,
            service=service,
            category=category,
            sub_category=sub_category,
            amount=amount,
            sql_query=sql_query,
        )

        create_billing_rule.additional_properties = d
        return create_billing_rule

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
