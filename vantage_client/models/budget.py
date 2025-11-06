from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_performance import BudgetPerformance
    from ..models.budget_period import BudgetPeriod


T = TypeVar("T", bound="Budget")


@_attrs_define
class Budget:
    """Budget model

    Attributes:
        token (str | Unset):
        name (str | Unset): The name of the Budget. Example: Acme123 Budget.
        workspace_token (str | Unset): The token for the Workspace the Budget is a part of.
        user_token (str | Unset): The token for the User who created this Budget.
        created_by_token (str | Unset): The token of the Creator of the Budget.
        cost_report_token (str | Unset): The token of the Report associated with the Budget.
        created_at (str | Unset): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19T00:00:00Z.
        budget_alert_tokens (list[str] | Unset): The tokens of the BudgetAlerts associated with the Budget.
        child_budget_tokens (list[str] | Unset): The tokens of the child Budgets associated with the hierarchical
            Budget.
        periods (list[BudgetPeriod] | Unset): The budget periods associated with the Budget.
        performance (list[BudgetPerformance] | Unset): The historical performance of the Budget.
    """

    token: str | Unset = UNSET
    name: str | Unset = UNSET
    workspace_token: str | Unset = UNSET
    user_token: str | Unset = UNSET
    created_by_token: str | Unset = UNSET
    cost_report_token: str | Unset = UNSET
    created_at: str | Unset = UNSET
    budget_alert_tokens: list[str] | Unset = UNSET
    child_budget_tokens: list[str] | Unset = UNSET
    periods: list[BudgetPeriod] | Unset = UNSET
    performance: list[BudgetPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        workspace_token = self.workspace_token

        user_token = self.user_token

        created_by_token = self.created_by_token

        cost_report_token = self.cost_report_token

        created_at = self.created_at

        budget_alert_tokens: list[str] | Unset = UNSET
        if not isinstance(self.budget_alert_tokens, Unset):
            budget_alert_tokens = self.budget_alert_tokens

        child_budget_tokens: list[str] | Unset = UNSET
        if not isinstance(self.child_budget_tokens, Unset):
            child_budget_tokens = self.child_budget_tokens

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        performance: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = []
            for performance_item_data in self.performance:
                performance_item = performance_item_data.to_dict()
                performance.append(performance_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if user_token is not UNSET:
            field_dict["user_token"] = user_token
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if budget_alert_tokens is not UNSET:
            field_dict["budget_alert_tokens"] = budget_alert_tokens
        if child_budget_tokens is not UNSET:
            field_dict["child_budget_tokens"] = child_budget_tokens
        if periods is not UNSET:
            field_dict["periods"] = periods
        if performance is not UNSET:
            field_dict["performance"] = performance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_performance import BudgetPerformance
        from ..models.budget_period import BudgetPeriod

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        user_token = d.pop("user_token", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        budget_alert_tokens = cast(list[str], d.pop("budget_alert_tokens", UNSET))

        child_budget_tokens = cast(list[str], d.pop("child_budget_tokens", UNSET))

        _periods = d.pop("periods", UNSET)
        periods: list[BudgetPeriod] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = BudgetPeriod.from_dict(periods_item_data)

                periods.append(periods_item)

        _performance = d.pop("performance", UNSET)
        performance: list[BudgetPerformance] | Unset = UNSET
        if _performance is not UNSET:
            performance = []
            for performance_item_data in _performance:
                performance_item = BudgetPerformance.from_dict(performance_item_data)

                performance.append(performance_item)

        budget = cls(
            token=token,
            name=name,
            workspace_token=workspace_token,
            user_token=user_token,
            created_by_token=created_by_token,
            cost_report_token=cost_report_token,
            created_at=created_at,
            budget_alert_tokens=budget_alert_tokens,
            child_budget_tokens=child_budget_tokens,
            periods=periods,
            performance=performance,
        )

        budget.additional_properties = d
        return budget

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
