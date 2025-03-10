from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_billing_rule_type import CreateBillingRuleType

T = TypeVar("T", bound="CreateBillingRule")


@_attrs_define
class CreateBillingRule:
    """Create a Billing Rule.

    Attributes:
        type_ (CreateBillingRuleType): The type of the Billing Rule. Note: the values are case insensitive.
        title (str): The title of the Billing Rule.
        charge_type (str): The charge type of the Billing Rule.
        percentage (float): The percentage of the cost shown. Example value: 75.0
        service (str): The service of the Billing Rule.
        category (str): The category of the Billing Rule.
        sub_category (str): The subcategory of the Billing Rule.
        start_period (str): The start period of the Billing Rule.
        amount (float): The amount for the Billing Rule. Example value: 300
    """

    type_: CreateBillingRuleType
    title: str
    charge_type: str
    percentage: float
    service: str
    category: str
    sub_category: str
    start_period: str
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

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
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "charge_type": charge_type,
                "percentage": percentage,
                "service": service,
                "category": category,
                "sub_category": sub_category,
                "start_period": start_period,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = CreateBillingRuleType(d.pop("type"))

        title = d.pop("title")

        charge_type = d.pop("charge_type")

        percentage = d.pop("percentage")

        service = d.pop("service")

        category = d.pop("category")

        sub_category = d.pop("sub_category")

        start_period = d.pop("start_period")

        amount = d.pop("amount")

        create_billing_rule = cls(
            type_=type_,
            title=title,
            charge_type=charge_type,
            percentage=percentage,
            service=service,
            category=category,
            sub_category=sub_category,
            start_period=start_period,
            amount=amount,
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
