from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """Invoice model

    Attributes:
        token (str | Unset):
        invoice_number (str | Unset): Sequential invoice number for the MSP account
        total (str | Unset): Total amount for the invoice period
        billing_period_start (str | Unset): Start date of the billing period. ISO 8601 formatted.
        billing_period_end (str | Unset): End date of the billing period. ISO 8601 formatted.
        status (str | Unset): Current status of the invoice
        created_at (str | Unset): The date and time, in UTC, the invoice was created. ISO 8601 formatted.
        updated_at (str | Unset): The date and time, in UTC, the invoice was last updated. ISO 8601 formatted.
        account_token (str | Unset): Token of the managed account this invoice belongs to
        account_name (str | Unset): Name of the managed account this invoice belongs to
        msp_account_token (str | Unset): Token of the MSP account that owns this invoice
    """

    token: str | Unset = UNSET
    invoice_number: str | Unset = UNSET
    total: str | Unset = UNSET
    billing_period_start: str | Unset = UNSET
    billing_period_end: str | Unset = UNSET
    status: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    account_token: str | Unset = UNSET
    account_name: str | Unset = UNSET
    msp_account_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        invoice_number = self.invoice_number

        total = self.total

        billing_period_start = self.billing_period_start

        billing_period_end = self.billing_period_end

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        account_token = self.account_token

        account_name = self.account_name

        msp_account_token = self.msp_account_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if total is not UNSET:
            field_dict["total"] = total
        if billing_period_start is not UNSET:
            field_dict["billing_period_start"] = billing_period_start
        if billing_period_end is not UNSET:
            field_dict["billing_period_end"] = billing_period_end
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if account_token is not UNSET:
            field_dict["account_token"] = account_token
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if msp_account_token is not UNSET:
            field_dict["msp_account_token"] = msp_account_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        invoice_number = d.pop("invoice_number", UNSET)

        total = d.pop("total", UNSET)

        billing_period_start = d.pop("billing_period_start", UNSET)

        billing_period_end = d.pop("billing_period_end", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        account_token = d.pop("account_token", UNSET)

        account_name = d.pop("account_name", UNSET)

        msp_account_token = d.pop("msp_account_token", UNSET)

        invoice = cls(
            token=token,
            invoice_number=invoice_number,
            total=total,
            billing_period_start=billing_period_start,
            billing_period_end=billing_period_end,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            account_token=account_token,
            account_name=account_name,
            msp_account_token=msp_account_token,
        )

        invoice.additional_properties = d
        return invoice

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
