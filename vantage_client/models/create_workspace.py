from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workspace_exchange_rate_date import CreateWorkspaceExchangeRateDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspace")


@_attrs_define
class CreateWorkspace:
    """Create a workspace

    Attributes:
        name (str): Name of the workspace.
        enable_currency_conversion (bool | Unset): Enable currency conversion for the workspace. Default: True.
        currency (str | Unset): Currency code for the workspace.
        exchange_rate_date (CreateWorkspaceExchangeRateDate | Unset): The date to use for currency conversion. Default:
            CreateWorkspaceExchangeRateDate.DAILY_RATE.
    """

    name: str
    enable_currency_conversion: bool | Unset = True
    currency: str | Unset = UNSET
    exchange_rate_date: CreateWorkspaceExchangeRateDate | Unset = CreateWorkspaceExchangeRateDate.DAILY_RATE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable_currency_conversion = self.enable_currency_conversion

        currency = self.currency

        exchange_rate_date: str | Unset = UNSET
        if not isinstance(self.exchange_rate_date, Unset):
            exchange_rate_date = self.exchange_rate_date.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if enable_currency_conversion is not UNSET:
            field_dict["enable_currency_conversion"] = enable_currency_conversion
        if currency is not UNSET:
            field_dict["currency"] = currency
        if exchange_rate_date is not UNSET:
            field_dict["exchange_rate_date"] = exchange_rate_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        enable_currency_conversion = d.pop("enable_currency_conversion", UNSET)

        currency = d.pop("currency", UNSET)

        _exchange_rate_date = d.pop("exchange_rate_date", UNSET)
        exchange_rate_date: CreateWorkspaceExchangeRateDate | Unset
        if isinstance(_exchange_rate_date, Unset):
            exchange_rate_date = UNSET
        else:
            exchange_rate_date = CreateWorkspaceExchangeRateDate(_exchange_rate_date)

        create_workspace = cls(
            name=name,
            enable_currency_conversion=enable_currency_conversion,
            currency=currency,
            exchange_rate_date=exchange_rate_date,
        )

        create_workspace.additional_properties = d
        return create_workspace

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
