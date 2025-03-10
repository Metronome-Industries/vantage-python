from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_rule import BillingRule
    from ..models.links import Links


T = TypeVar("T", bound="BillingRules")


@_attrs_define
class BillingRules:
    """BillingRules model

    Attributes:
        links (Union[Unset, Links]):
        billing_rules (Union[Unset, list['BillingRule']]):
    """

    links: Union[Unset, "Links"] = UNSET
    billing_rules: Union[Unset, list["BillingRule"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        billing_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_rules, Unset):
            billing_rules = []
            for billing_rules_item_data in self.billing_rules:
                billing_rules_item = billing_rules_item_data.to_dict()
                billing_rules.append(billing_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if billing_rules is not UNSET:
            field_dict["billing_rules"] = billing_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.billing_rule import BillingRule
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        billing_rules = []
        _billing_rules = d.pop("billing_rules", UNSET)
        for billing_rules_item_data in _billing_rules or []:
            billing_rules_item = BillingRule.from_dict(billing_rules_item_data)

            billing_rules.append(billing_rules_item)

        billing_rules = cls(
            links=links,
            billing_rules=billing_rules,
        )

        billing_rules.additional_properties = d
        return billing_rules

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
