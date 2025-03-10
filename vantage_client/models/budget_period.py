from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetPeriod")


@_attrs_define
class BudgetPeriod:
    """
    Attributes:
        start_at (Union[Unset, str]): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        end_at (Union[Unset, str]): The date and time, in UTC, the Budget was created. ISO 8601 Formatted. Example:
            2024-03-19 00:00:00+00:00.
        amount (Union[Unset, str]): The amount of the Budget Period as a string to ensure precision. Example: 100.00.
    """

    start_at: Union[Unset, str] = UNSET
    end_at: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at

        end_at = self.end_at

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        amount = d.pop("amount", UNSET)

        budget_period = cls(
            start_at=start_at,
            end_at=end_at,
            amount=amount,
        )

        budget_period.additional_properties = d
        return budget_period

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
