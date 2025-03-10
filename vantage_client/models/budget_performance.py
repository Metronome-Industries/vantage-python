from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetPerformance")


@_attrs_define
class BudgetPerformance:
    """
    Attributes:
        date (Union[Unset, str]): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        actual (Union[Unset, str]): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        amount (Union[Unset, str]): The amount of the Budget Period as a string to ensure precision. Example: 100.00.
    """

    date: Union[Unset, str] = UNSET
    actual: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        actual = self.actual

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if actual is not UNSET:
            field_dict["actual"] = actual
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        actual = d.pop("actual", UNSET)

        amount = d.pop("amount", UNSET)

        budget_performance = cls(
            date=date,
            actual=actual,
            amount=amount,
        )

        budget_performance.additional_properties = d
        return budget_performance

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
