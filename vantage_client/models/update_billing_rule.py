from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillingRule")


@_attrs_define
class UpdateBillingRule:
    """Update a Billing Rule.

    Attributes:
        title (Union[Unset, str]): The title of the Billing Rule.
        charge_type (Union[Unset, str]): The charge type of the Billing Rule.
        percentage (Union[Unset, float]): The percentage of the cost shown. Example value: 75.0
        service (Union[Unset, str]): The service of the Billing Rule.
        category (Union[Unset, str]): The category of the Billing Rule.
        sub_category (Union[Unset, str]): The subcategory of the Billing Rule.
        start_period (Union[Unset, str]): The start period of the Billing Rule.
        amount (Union[Unset, float]): The credit amount for the Billing Rule. Example value: 300
    """

    title: Union[Unset, str] = UNSET
    charge_type: Union[Unset, str] = UNSET
    percentage: Union[Unset, float] = UNSET
    service: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    sub_category: Union[Unset, str] = UNSET
    start_period: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        charge_type = d.pop("charge_type", UNSET)

        percentage = d.pop("percentage", UNSET)

        service = d.pop("service", UNSET)

        category = d.pop("category", UNSET)

        sub_category = d.pop("sub_category", UNSET)

        start_period = d.pop("start_period", UNSET)

        amount = d.pop("amount", UNSET)

        update_billing_rule = cls(
            title=title,
            charge_type=charge_type,
            percentage=percentage,
            service=service,
            category=category,
            sub_category=sub_category,
            start_period=start_period,
            amount=amount,
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
