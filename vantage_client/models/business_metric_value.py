from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessMetricValue")


@_attrs_define
class BusinessMetricValue:
    """
    Attributes:
        date (Union[Unset, str]): The date of the Business Metric Value. ISO 8601 formatted. Example: 2024-03-01+00:00.
        amount (Union[Unset, str]): The amount of the Business Metric Value as a string to ensure precision. Example:
            100.00.
        label (Union[Unset, str]): The label of the Business Metric Value. Example: Cost Center A.
    """

    date: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        amount = self.amount

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        amount = d.pop("amount", UNSET)

        label = d.pop("label", UNSET)

        business_metric_value = cls(
            date=date,
            amount=amount,
            label=label,
        )

        business_metric_value.additional_properties = d
        return business_metric_value

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
