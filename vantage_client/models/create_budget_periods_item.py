from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBudgetPeriodsItem")


@_attrs_define
class CreateBudgetPeriodsItem:
    """
    Attributes:
        start_at (datetime.date): The start date of the period.
        amount (float): The amount of the period.
        end_at (datetime.date | None | Unset): The end date of the period.
    """

    start_at: datetime.date
    amount: float
    end_at: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        amount = self.amount

        end_at: None | str | Unset
        if isinstance(self.end_at, Unset):
            end_at = UNSET
        elif isinstance(self.end_at, datetime.date):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "amount": amount,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = isoparse(d.pop("start_at")).date()

        amount = d.pop("amount")

        def _parse_end_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = isoparse(data).date()

                return end_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_at = _parse_end_at(d.pop("end_at", UNSET))

        create_budget_periods_item = cls(
            start_at=start_at,
            amount=amount,
            end_at=end_at,
        )

        create_budget_periods_item.additional_properties = d
        return create_budget_periods_item

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
