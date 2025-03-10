from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_workspace_files_body_currency import UpdateWorkspaceFilesBodyCurrency
from ..models.update_workspace_files_body_exchange_rate_date import UpdateWorkspaceFilesBodyExchangeRateDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkspaceFilesBody")


@_attrs_define
class UpdateWorkspaceFilesBody:
    """
    Attributes:
        name (Union[Unset, str]): Name of the workspace.
        enable_currency_conversion (Union[Unset, bool]): Enable currency conversion for the workspace. Default: True.
        currency (Union[Unset, UpdateWorkspaceFilesBodyCurrency]): Currency code for the workspace.
        exchange_rate_date (Union[Unset, UpdateWorkspaceFilesBodyExchangeRateDate]): The date to use for currency
            conversion. Default: UpdateWorkspaceFilesBodyExchangeRateDate.DAILY_RATE.
    """

    name: Union[Unset, str] = UNSET
    enable_currency_conversion: Union[Unset, bool] = True
    currency: Union[Unset, UpdateWorkspaceFilesBodyCurrency] = UNSET
    exchange_rate_date: Union[Unset, UpdateWorkspaceFilesBodyExchangeRateDate] = (
        UpdateWorkspaceFilesBodyExchangeRateDate.DAILY_RATE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable_currency_conversion = self.enable_currency_conversion

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        exchange_rate_date: Union[Unset, str] = UNSET
        if not isinstance(self.exchange_rate_date, Unset):
            exchange_rate_date = self.exchange_rate_date.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enable_currency_conversion is not UNSET:
            field_dict["enable_currency_conversion"] = enable_currency_conversion
        if currency is not UNSET:
            field_dict["currency"] = currency
        if exchange_rate_date is not UNSET:
            field_dict["exchange_rate_date"] = exchange_rate_date

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        enable_currency_conversion = (
            self.enable_currency_conversion
            if isinstance(self.enable_currency_conversion, Unset)
            else (None, str(self.enable_currency_conversion).encode(), "text/plain")
        )

        currency: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = (None, str(self.currency.value).encode(), "text/plain")

        exchange_rate_date: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.exchange_rate_date, Unset):
            exchange_rate_date = (None, str(self.exchange_rate_date.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        name = d.pop("name", UNSET)

        enable_currency_conversion = d.pop("enable_currency_conversion", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, UpdateWorkspaceFilesBodyCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = UpdateWorkspaceFilesBodyCurrency(_currency)

        _exchange_rate_date = d.pop("exchange_rate_date", UNSET)
        exchange_rate_date: Union[Unset, UpdateWorkspaceFilesBodyExchangeRateDate]
        if isinstance(_exchange_rate_date, Unset):
            exchange_rate_date = UNSET
        else:
            exchange_rate_date = UpdateWorkspaceFilesBodyExchangeRateDate(_exchange_rate_date)

        update_workspace_files_body = cls(
            name=name,
            enable_currency_conversion=enable_currency_conversion,
            currency=currency,
            exchange_rate_date=exchange_rate_date,
        )

        update_workspace_files_body.additional_properties = d
        return update_workspace_files_body

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
