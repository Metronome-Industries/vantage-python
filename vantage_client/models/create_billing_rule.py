from collections.abc import Mapping
from typing import Any, TypeVar, Union

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
        start_period (Union[Unset, str]): The start period of the BillingRule. DEPRECATED: use start_date instead.
        start_date (Union[Unset, str]): The start date of the BillingRule. ISO 8601 formatted.
        end_date (Union[Unset, str]): The end date of the BillingRule. ISO 8601 formatted.
        apply_to_all (Union[Unset, bool]): Determines if the BillingRule applies to all current and future managed
            accounts.
        charge_type (Union[Unset, str]): The charge type of the BillingRule. Required for Exclusion rules.
        percentage (Union[Unset, float]): The percentage of the cost shown. Required for Adjustment rules. Example
            value: 75.0
        service (Union[Unset, str]): The service of the BillingRule. Required for Charge and Credit rules.
        category (Union[Unset, str]): The category of the BillingRule. Required for Charge and Credit rules.
        sub_category (Union[Unset, str]): The subcategory of the BillingRule. Required for Charge and Credit rules.
        amount (Union[Unset, float]): The amount for the BillingRule. Required for Charge and Credit rules. Example
            value: 300
        sql_query (Union[Unset, str]): The SQL query for the BillingRule. Required for Custom rules. Example value:
            UPDATE costs SET costs.amount = costs.amount * 0.95
    """

    type_: CreateBillingRuleType
    title: str
    start_period: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    apply_to_all: Union[Unset, bool] = UNSET
    charge_type: Union[Unset, str] = UNSET
    percentage: Union[Unset, float] = UNSET
    service: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    sub_category: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    sql_query: Union[Unset, str] = UNSET
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
