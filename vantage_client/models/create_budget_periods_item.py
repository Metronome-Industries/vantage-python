import datetime
from typing import Any, TypeVar, Union, cast

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
        end_at (Union[None, Unset, datetime.date]): The end date of the period.
    """

    start_at: datetime.date
    amount: float
    end_at: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        amount = self.amount

        end_at: Union[None, Unset, str]
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        start_at = isoparse(d.pop("start_at")).date()

        amount = d.pop("amount")

        def _parse_end_at(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = isoparse(data).date()

                return end_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

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
