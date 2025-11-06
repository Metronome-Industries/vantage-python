from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_status import IntegrationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Integration")


@_attrs_define
class Integration:
    """Integration model

    Attributes:
        token (str | Unset):
        provider (str | Unset): The name of the Integration. Example: AWS.
        account_identifier (str | Unset): The account identifier. For GCP this is the billing Account ID, for Azure this
            is the account ID Example: 011389-EF4C3E-3ED7AE.
        status (IntegrationStatus | Unset): The status of the Integration. Can be 'connected', 'error', 'pending',
            'importing', 'imported', or 'disconnected'. Example: imported.
        last_updated (str | Unset): The date and time, in UTC, when the Integration was last updated. ISO 8601
            Formatted. Example: 2023-08-04T00:00:00Z.
        workspace_tokens (list[str] | Unset): The tokens for any Workspaces that the account belongs to.
        created_at (str | Unset): The date and time, in UTC, the Integration was created. ISO 8601 Formatted. Example:
            2023-08-04T00:00:00Z.
    """

    token: str | Unset = UNSET
    provider: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    status: IntegrationStatus | Unset = UNSET
    last_updated: str | Unset = UNSET
    workspace_tokens: list[str] | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        provider = self.provider

        account_identifier = self.account_identifier

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_updated = self.last_updated

        workspace_tokens: list[str] | Unset = UNSET
        if not isinstance(self.workspace_tokens, Unset):
            workspace_tokens = self.workspace_tokens

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if provider is not UNSET:
            field_dict["provider"] = provider
        if account_identifier is not UNSET:
            field_dict["account_identifier"] = account_identifier
        if status is not UNSET:
            field_dict["status"] = status
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if workspace_tokens is not UNSET:
            field_dict["workspace_tokens"] = workspace_tokens
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        provider = d.pop("provider", UNSET)

        account_identifier = d.pop("account_identifier", UNSET)

        _status = d.pop("status", UNSET)
        status: IntegrationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IntegrationStatus(_status)

        last_updated = d.pop("last_updated", UNSET)

        workspace_tokens = cast(list[str], d.pop("workspace_tokens", UNSET))

        created_at = d.pop("created_at", UNSET)

        integration = cls(
            token=token,
            provider=provider,
            account_identifier=account_identifier,
            status=status,
            last_updated=last_updated,
            workspace_tokens=workspace_tokens,
            created_at=created_at,
        )

        integration.additional_properties = d
        return integration

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
