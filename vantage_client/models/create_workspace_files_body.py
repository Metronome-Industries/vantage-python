from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workspace_files_body_exchange_rate_date import CreateWorkspaceFilesBodyExchangeRateDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceFilesBody")


@_attrs_define
class CreateWorkspaceFilesBody:
    """
    Attributes:
        name (str): Name of the workspace.
        enable_currency_conversion (Union[Unset, bool]): Enable currency conversion for the workspace. Default: True.
        currency (Union[Unset, str]): Currency code for the workspace.
        exchange_rate_date (Union[Unset, CreateWorkspaceFilesBodyExchangeRateDate]): The date to use for currency
            conversion. Default: CreateWorkspaceFilesBodyExchangeRateDate.DAILY_RATE.
    """

    name: str
    enable_currency_conversion: Union[Unset, bool] = True
    currency: Union[Unset, str] = UNSET
    exchange_rate_date: Union[Unset, CreateWorkspaceFilesBodyExchangeRateDate] = (
        CreateWorkspaceFilesBodyExchangeRateDate.DAILY_RATE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable_currency_conversion = self.enable_currency_conversion

        currency = self.currency

        exchange_rate_date: Union[Unset, str] = UNSET
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

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        enable_currency_conversion = (
            self.enable_currency_conversion
            if isinstance(self.enable_currency_conversion, Unset)
            else (None, str(self.enable_currency_conversion).encode(), "text/plain")
        )

        currency = (
            self.currency if isinstance(self.currency, Unset) else (None, str(self.currency).encode(), "text/plain")
        )

        exchange_rate_date: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.exchange_rate_date, Unset):
            exchange_rate_date = (None, str(self.exchange_rate_date.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        enable_currency_conversion = d.pop("enable_currency_conversion", UNSET)

        currency = d.pop("currency", UNSET)

        _exchange_rate_date = d.pop("exchange_rate_date", UNSET)
        exchange_rate_date: Union[Unset, CreateWorkspaceFilesBodyExchangeRateDate]
        if isinstance(_exchange_rate_date, Unset):
            exchange_rate_date = UNSET
        else:
            exchange_rate_date = CreateWorkspaceFilesBodyExchangeRateDate(_exchange_rate_date)

        create_workspace_files_body = cls(
            name=name,
            enable_currency_conversion=enable_currency_conversion,
            currency=currency,
            exchange_rate_date=exchange_rate_date,
        )

        create_workspace_files_body.additional_properties = d
        return create_workspace_files_body

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
