from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingRule")


@_attrs_define
class BillingRule:
    """BillingRule model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the BillingRule. Example: Credit for Unused EC2 Instances.
        type_ (Union[Unset, str]): The type of the BillingRule. Example: credit.
        start_date (Union[Unset, str]): The start date of the BillingRule. Example: 2024-06-28T00:00:00Z.
        end_date (Union[Unset, str]): The end date of the BillingRule. Example: 2024-06-28T00:00:00Z.
        apply_to_all (Union[Unset, bool]): Whether the BillingRule applies to all future managed accounts. Example:
            True.
        created_by_token (Union[Unset, str]): The token of the Creator of the BillingRule. Example: usr_1234.
        created_at (Union[Unset, str]): The date and time, in UTC, the BillingRule was created. ISO 8601 Formatted.
            Example: 2024-06-28T00:00:00Z.
        service (Union[Unset, str]): The service for the BillingRule (Charge). Example: AWS Cloudfront.
        category (Union[Unset, str]): The category for the BillingRule (Charge). Example: MSP Fee.
        percentage (Union[Unset, str]): The percentage of the cost shown for the BillingRule (Adjustment). Example:
            75.0.
        charge_type (Union[Unset, str]): The charge type for the BillingRule. Example: RIFee.
        sub_category (Union[Unset, str]): The subcategory for the BillingRule (Charge). Example: One-time.
        start_period (Union[Unset, str]): The start period for the BillingRule (Charge). Example: 2024-05-01.
        amount (Union[Unset, str]): The amount for the BillingRule (Charge). Example: 5000.25.
        sql_query (Union[Unset, str]): The SQL query for the BillingRule (Custom). Example: UPDATE costs SET
            costs.amount = costs.amount * 0.95.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    apply_to_all: Union[Unset, bool] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    percentage: Union[Unset, str] = UNSET
    charge_type: Union[Unset, str] = UNSET
    sub_category: Union[Unset, str] = UNSET
    start_period: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    sql_query: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        type_ = self.type_

        start_date = self.start_date

        end_date = self.end_date

        apply_to_all = self.apply_to_all

        created_by_token = self.created_by_token

        created_at = self.created_at

        service = self.service

        category = self.category

        percentage = self.percentage

        charge_type = self.charge_type

        sub_category = self.sub_category

        start_period = self.start_period

        amount = self.amount

        sql_query = self.sql_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if apply_to_all is not UNSET:
            field_dict["apply_to_all"] = apply_to_all
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if service is not UNSET:
            field_dict["service"] = service
        if category is not UNSET:
            field_dict["category"] = category
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if charge_type is not UNSET:
            field_dict["charge_type"] = charge_type
        if sub_category is not UNSET:
            field_dict["sub_category"] = sub_category
        if start_period is not UNSET:
            field_dict["start_period"] = start_period
        if amount is not UNSET:
            field_dict["amount"] = amount
        if sql_query is not UNSET:
            field_dict["sql_query"] = sql_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        apply_to_all = d.pop("apply_to_all", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        service = d.pop("service", UNSET)

        category = d.pop("category", UNSET)

        percentage = d.pop("percentage", UNSET)

        charge_type = d.pop("charge_type", UNSET)

        sub_category = d.pop("sub_category", UNSET)

        start_period = d.pop("start_period", UNSET)

        amount = d.pop("amount", UNSET)

        sql_query = d.pop("sql_query", UNSET)

        billing_rule = cls(
            token=token,
            title=title,
            type_=type_,
            start_date=start_date,
            end_date=end_date,
            apply_to_all=apply_to_all,
            created_by_token=created_by_token,
            created_at=created_at,
            service=service,
            category=category,
            percentage=percentage,
            charge_type=charge_type,
            sub_category=sub_category,
            start_period=start_period,
            amount=amount,
            sql_query=sql_query,
        )

        billing_rule.additional_properties = d
        return billing_rule

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
