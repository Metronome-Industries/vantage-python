from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """Workspace model

    Attributes:
        token (Union[Unset, str]):
        name (Union[Unset, str]): The name of the Workspace. Example: Acme Corp..
        created_at (Union[Unset, str]): The date and time, in UTC, the Workspace was created. ISO 8601 Formatted.
            Example: 2023-08-04 00:00:00+00:00.
        enable_currency_conversion (Union[Unset, bool]): Whether or not currency conversion is enabled for the
            Workspace.
        currency (Union[Unset, str]): The currency code for the Workspace that will be used for currency conversion.
            Example: USD.
        exchange_rate_date (Union[Unset, str]): The exchange rate date that will be used to convert currency for your
            cost data.
    """

    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    enable_currency_conversion: Union[Unset, bool] = UNSET
    currency: Union[Unset, str] = UNSET
    exchange_rate_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        created_at = self.created_at

        enable_currency_conversion = self.enable_currency_conversion

        currency = self.currency

        exchange_rate_date = self.exchange_rate_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enable_currency_conversion is not UNSET:
            field_dict["enable_currency_conversion"] = enable_currency_conversion
        if currency is not UNSET:
            field_dict["currency"] = currency
        if exchange_rate_date is not UNSET:
            field_dict["exchange_rate_date"] = exchange_rate_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        created_at = d.pop("created_at", UNSET)

        enable_currency_conversion = d.pop("enable_currency_conversion", UNSET)

        currency = d.pop("currency", UNSET)

        exchange_rate_date = d.pop("exchange_rate_date", UNSET)

        workspace = cls(
            token=token,
            name=name,
            created_at=created_at,
            enable_currency_conversion=enable_currency_conversion,
            currency=currency,
            exchange_rate_date=exchange_rate_date,
        )

        workspace.additional_properties = d
        return workspace

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
