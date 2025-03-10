from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        token (Union[Unset, str]):
        name (Union[Unset, str]): The name of the Budget. Example: Acme123 Budget.
        workspace_token (Union[Unset, str]): The token for the Workspace the Budget is a part of.
        user_token (Union[Unset, str]): The token for the User who created this Budget.
        created_by_token (Union[Unset, str]): The token of the Creator of the Budget.
        cost_report_token (Union[Unset, str]): The token of the Report associated with the Budget.
        created_at (Union[Unset, str]): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        budget_alert_tokens (Union[Unset, list[str]]): The tokens of the BudgetAlerts associated with the Budget.
        child_budget_tokens (Union[Unset, list[str]]): The tokens of the child Budgets associated with the hierarchical
            Budget.
        periods (Union[Unset, list['BudgetPeriod']]): The budget periods associated with the Budget.
        performance (Union[Unset, list['BudgetPerformance']]): The historical performance of the Budget.
    """

    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    user_token: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    cost_report_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    budget_alert_tokens: Union[Unset, list[str]] = UNSET
    child_budget_tokens: Union[Unset, list[str]] = UNSET
    periods: Union[Unset, list["BudgetPeriod"]] = UNSET
    performance: Union[Unset, list["BudgetPerformance"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        workspace_token = self.workspace_token

        user_token = self.user_token

        created_by_token = self.created_by_token

        cost_report_token = self.cost_report_token

        created_at = self.created_at

        budget_alert_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.budget_alert_tokens, Unset):
            budget_alert_tokens = self.budget_alert_tokens

        child_budget_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.child_budget_tokens, Unset):
            child_budget_tokens = self.child_budget_tokens

        periods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        performance: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.budget_performance import BudgetPerformance
        from ..models.budget_period import BudgetPeriod

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        user_token = d.pop("user_token", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        cost_report_token = d.pop("cost_report_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        budget_alert_tokens = cast(list[str], d.pop("budget_alert_tokens", UNSET))

        child_budget_tokens = cast(list[str], d.pop("child_budget_tokens", UNSET))

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = BudgetPeriod.from_dict(periods_item_data)

            periods.append(periods_item)

        performance = []
        _performance = d.pop("performance", UNSET)
        for performance_item_data in _performance or []:
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
