from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialCommitment")


@_attrs_define
class FinancialCommitment:
    """
    Attributes:
        commitment_type (Union[Unset, str]): The commitment type (eg Savings Plan or Reserved Instance). Example:
            Savings Plan.
        service (Union[Unset, str]): The service this commitment applies towards. Example: Compute.
        account (Union[Unset, str]): The account for this financial commitment. Example: 113074892135.
        type_ (Union[Unset, str]): The type of financial commitment. Example: m5.large.
        amount (Union[Unset, str]): The number of instances for the financial commitment. Example: 4.
        term (Union[Unset, str]): The duration in years of the financial commitment. Example: 3 Year.
        payment_type (Union[Unset, str]): The type of payment for the financial commitment. Example: No upfront.
        region (Union[Unset, str]): The region for the financial commitment. Example: us-east-1.
        purchase_date (Union[Unset, str]): The purchase date of the financial commitment. ISO 8601 Formatted. Example:
            2023-08-30.
        expiration_date (Union[Unset, str]): The expiration date of the financial commitment. ISO 8601 Formatted.
            Example: 2026-08-30.
        commitment (Union[Unset, str]): The amount of the financial commitment. Example: $2.18.
        status (Union[Unset, str]): The status of the financial commitment (e.g. active vs expired). Example: active.
        created_at (Union[Unset, str]): The date and time, in UTC, the Financial Commitment was created. ISO 8601
            Formatted. Example: 2024-03-19 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the FinancialCommitment is a part of.
    """

    commitment_type: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    term: Union[Unset, str] = UNSET
    payment_type: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, str] = UNSET
    commitment: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commitment_type = self.commitment_type

        service = self.service

        account = self.account

        type_ = self.type_

        amount = self.amount

        term = self.term

        payment_type = self.payment_type

        region = self.region

        purchase_date = self.purchase_date

        expiration_date = self.expiration_date

        commitment = self.commitment

        status = self.status

        created_at = self.created_at

        workspace_token = self.workspace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commitment_type is not UNSET:
            field_dict["commitment_type"] = commitment_type
        if service is not UNSET:
            field_dict["service"] = service
        if account is not UNSET:
            field_dict["account"] = account
        if type_ is not UNSET:
            field_dict["type"] = type_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if term is not UNSET:
            field_dict["term"] = term
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if region is not UNSET:
            field_dict["region"] = region
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if commitment is not UNSET:
            field_dict["commitment"] = commitment
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        commitment_type = d.pop("commitment_type", UNSET)

        service = d.pop("service", UNSET)

        account = d.pop("account", UNSET)

        type_ = d.pop("type", UNSET)

        amount = d.pop("amount", UNSET)

        term = d.pop("term", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        region = d.pop("region", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        expiration_date = d.pop("expiration_date", UNSET)

        commitment = d.pop("commitment", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        financial_commitment = cls(
            commitment_type=commitment_type,
            service=service,
            account=account,
            type_=type_,
            amount=amount,
            term=term,
            payment_type=payment_type,
            region=region,
            purchase_date=purchase_date,
            expiration_date=expiration_date,
            commitment=commitment,
            status=status,
            created_at=created_at,
            workspace_token=workspace_token,
        )

        financial_commitment.additional_properties = d
        return financial_commitment

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
