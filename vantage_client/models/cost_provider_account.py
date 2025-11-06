from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostProviderAccount")


@_attrs_define
class CostProviderAccount:
    """
    Attributes:
        title (str | Unset): The display name of the provider account. Example: Production Account.
        account_id (str | Unset): The provider account identifier (e.g., AWS account ID, Azure subscription ID).
            Example: 123456789012.
        provider_uuid (str | Unset): The provider-specific unique identifier. Example:
            arn:aws:organizations::123456789012:account/o-example12345/123456789012.
        provider (str | Unset): The provider type (aws, azure, gcp, etc.). Example: aws.
    """

    title: str | Unset = UNSET
    account_id: str | Unset = UNSET
    provider_uuid: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        account_id = self.account_id

        provider_uuid = self.provider_uuid

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if provider_uuid is not UNSET:
            field_dict["provider_uuid"] = provider_uuid
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        account_id = d.pop("account_id", UNSET)

        provider_uuid = d.pop("provider_uuid", UNSET)

        provider = d.pop("provider", UNSET)

        cost_provider_account = cls(
            title=title,
            account_id=account_id,
            provider_uuid=provider_uuid,
            provider=provider,
        )

        cost_provider_account.additional_properties = d
        return cost_provider_account

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
