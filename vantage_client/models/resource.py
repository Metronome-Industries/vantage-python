from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_cost import ResourceCost


T = TypeVar("T", bound="Resource")


@_attrs_define
class Resource:
    """Resource model

    Attributes:
        token (str | Unset):
        uuid (str | Unset): The unique identifier for the resource. Example: i-0a1b2c3d4e5f6g7h8.
        type_ (str | Unset): The kind of resource. Example: aws_instance.
        label (str | Unset):
        metadata (str | Unset): Type-specific attributes of the resource.
        account_id (str | Unset): The provider account where the resource is located.
        billing_account_id (str | Unset): The provider billing account this resource is charged to.
        provider (str | Unset): The provider of the resource. Example: aws.
        region (str | Unset): The region where the resource is located. Region values are specific to each provider.
            Example: us-west-2.
        costs (list[ResourceCost] | Unset): The cost of the resource broken down by category.
        created_at (str | Unset): The date and time when Vantage first observed the resource.
    """

    token: str | Unset = UNSET
    uuid: str | Unset = UNSET
    type_: str | Unset = UNSET
    label: str | Unset = UNSET
    metadata: str | Unset = UNSET
    account_id: str | Unset = UNSET
    billing_account_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    region: str | Unset = UNSET
    costs: list[ResourceCost] | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        uuid = self.uuid

        type_ = self.type_

        label = self.label

        metadata = self.metadata

        account_id = self.account_id

        billing_account_id = self.billing_account_id

        provider = self.provider

        region = self.region

        costs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.costs, Unset):
            costs = []
            for costs_item_data in self.costs:
                costs_item = costs_item_data.to_dict()
                costs.append(costs_item)

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if billing_account_id is not UNSET:
            field_dict["billing_account_id"] = billing_account_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if region is not UNSET:
            field_dict["region"] = region
        if costs is not UNSET:
            field_dict["costs"] = costs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_cost import ResourceCost

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        uuid = d.pop("uuid", UNSET)

        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        metadata = d.pop("metadata", UNSET)

        account_id = d.pop("account_id", UNSET)

        billing_account_id = d.pop("billing_account_id", UNSET)

        provider = d.pop("provider", UNSET)

        region = d.pop("region", UNSET)

        _costs = d.pop("costs", UNSET)
        costs: list[ResourceCost] | Unset = UNSET
        if _costs is not UNSET:
            costs = []
            for costs_item_data in _costs:
                costs_item = ResourceCost.from_dict(costs_item_data)

                costs.append(costs_item)

        created_at = d.pop("created_at", UNSET)

        resource = cls(
            token=token,
            uuid=uuid,
            type_=type_,
            label=label,
            metadata=metadata,
            account_id=account_id,
            billing_account_id=billing_account_id,
            provider=provider,
            region=region,
            costs=costs,
            created_at=created_at,
        )

        resource.additional_properties = d
        return resource

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
