from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_status import IntegrationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Integration")


@_attrs_define
class Integration:
    """Integration model

    Attributes:
        token (Union[Unset, str]):
        provider (Union[Unset, str]): The name of the Integration. Example: AWS.
        account_identifier (Union[Unset, str]): The account identifier. For GCP this is the billing Account ID, for
            Azure this is the account ID Example: 011389-EF4C3E-3ED7AE.
        status (Union[Unset, IntegrationStatus]): The status of the Integration. Can be 'connected' or 'disconnected'.
            Example: connected.
        workspace_tokens (Union[Unset, list[str]]): The tokens for any Workspaces that the account belongs to.
        created_at (Union[Unset, str]): The date and time, in UTC, the Integration was created. ISO 8601 Formatted.
            Example: 2023-08-04 00:00:00+00:00.
    """

    token: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    account_identifier: Union[Unset, str] = UNSET
    status: Union[Unset, IntegrationStatus] = UNSET
    workspace_tokens: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        provider = self.provider

        account_identifier = self.account_identifier

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        workspace_tokens: Union[Unset, list[str]] = UNSET
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
        if workspace_tokens is not UNSET:
            field_dict["workspace_tokens"] = workspace_tokens
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        provider = d.pop("provider", UNSET)

        account_identifier = d.pop("account_identifier", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IntegrationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IntegrationStatus(_status)

        workspace_tokens = cast(list[str], d.pop("workspace_tokens", UNSET))

        created_at = d.pop("created_at", UNSET)

        integration = cls(
            token=token,
            provider=provider,
            account_identifier=account_identifier,
            status=status,
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
