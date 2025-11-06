from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Recommendation")


@_attrs_define
class Recommendation:
    """Recommendation model

    Attributes:
        token (str | Unset):
        category (str | Unset): The category of the Recommendation. Example: ec2_compute_optimizer_recommender.
        workspace_token (str | Unset): The token for the Workspace the Recommendation is a part of.
        provider (str | Unset): The provider the Recommendation is for.
        provider_account_id (str | Unset): The account ID of the provider. For Azure, this is the subscription ID.
        description (str | Unset):
        potential_savings (str | Unset): The monthly potential savings of the Recommendation. Example: 100.00.
        service (str | Unset): The service the Recommendation is for. Example: Amazon EC2.
        created_at (str | Unset): The date and time, in UTC, the Recommendation was created. ISO 8601 Formatted.
        resources_affected_count (str | Unset): The number of ProviderResources related to the Recommendation. Use the
            `recommendations/:token/resources` endpoint to get the full list of resources.
    """

    token: str | Unset = UNSET
    category: str | Unset = UNSET
    workspace_token: str | Unset = UNSET
    provider: str | Unset = UNSET
    provider_account_id: str | Unset = UNSET
    description: str | Unset = UNSET
    potential_savings: str | Unset = UNSET
    service: str | Unset = UNSET
    created_at: str | Unset = UNSET
    resources_affected_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        category = self.category

        workspace_token = self.workspace_token

        provider = self.provider

        provider_account_id = self.provider_account_id

        description = self.description

        potential_savings = self.potential_savings

        service = self.service

        created_at = self.created_at

        resources_affected_count = self.resources_affected_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if category is not UNSET:
            field_dict["category"] = category
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_account_id is not UNSET:
            field_dict["provider_account_id"] = provider_account_id
        if description is not UNSET:
            field_dict["description"] = description
        if potential_savings is not UNSET:
            field_dict["potential_savings"] = potential_savings
        if service is not UNSET:
            field_dict["service"] = service
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if resources_affected_count is not UNSET:
            field_dict["resources_affected_count"] = resources_affected_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        category = d.pop("category", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        provider = d.pop("provider", UNSET)

        provider_account_id = d.pop("provider_account_id", UNSET)

        description = d.pop("description", UNSET)

        potential_savings = d.pop("potential_savings", UNSET)

        service = d.pop("service", UNSET)

        created_at = d.pop("created_at", UNSET)

        resources_affected_count = d.pop("resources_affected_count", UNSET)

        recommendation = cls(
            token=token,
            category=category,
            workspace_token=workspace_token,
            provider=provider,
            provider_account_id=provider_account_id,
            description=description,
            potential_savings=potential_savings,
            service=service,
            created_at=created_at,
            resources_affected_count=resources_affected_count,
        )

        recommendation.additional_properties = d
        return recommendation

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
