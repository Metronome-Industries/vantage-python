from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_budget_periods_item import UpdateBudgetPeriodsItem


T = TypeVar("T", bound="UpdateBudget")


@_attrs_define
class UpdateBudget:
    """Update a Budget.

    Attributes:
        name (Union[Unset, str]): The name of the Budget.
        cost_report_token (Union[Unset, str]): The CostReport token. Ignored for hierarchical Budgets.
        child_budget_tokens (Union[Unset, list[str]]): The tokens of any child Budgets when creating a hierarchical
            Budget.
        periods (Union[Unset, list['UpdateBudgetPeriodsItem']]): The periods for the Budget. The start_at and end_at
            must be iso8601 formatted e.g. YYYY-MM-DD. Ignored for hierarchical Budgets.
    """

    name: Union[Unset, str] = UNSET
    cost_report_token: Union[Unset, str] = UNSET
    child_budget_tokens: Union[Unset, list[str]] = UNSET
    periods: Union[Unset, list["UpdateBudgetPeriodsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cost_report_token = self.cost_report_token

        child_budget_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.child_budget_tokens, Unset):
            child_budget_tokens = self.child_budget_tokens

        periods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token
        if child_budget_tokens is not UNSET:
            field_dict["child_budget_tokens"] = child_budget_tokens
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_budget_periods_item import UpdateBudgetPeriodsItem

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        child_budget_tokens = cast(list[str], d.pop("child_budget_tokens", UNSET))

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = UpdateBudgetPeriodsItem.from_dict(periods_item_data)

            periods.append(periods_item)

        update_budget = cls(
            name=name,
            cost_report_token=cost_report_token,
            child_budget_tokens=child_budget_tokens,
            periods=periods,
        )

        update_budget.additional_properties = d
        return update_budget

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
