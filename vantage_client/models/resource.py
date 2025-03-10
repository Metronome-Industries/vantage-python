from typing import TYPE_CHECKING, Any, TypeVar, Union

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
        token (Union[Unset, str]):
        uuid (Union[Unset, str]): The unique identifier for the resource. Example: i-0a1b2c3d4e5f6g7h8.
        type_ (Union[Unset, str]): The kind of resource. Example: aws_instance.
        label (Union[Unset, str]):
        metadata (Union[Unset, str]): Type-specific attributes of the resource.
        account_id (Union[Unset, str]): The provider account where the resource is located.
        billing_account_id (Union[Unset, str]): The provider billing account this resource is charged to.
        provider (Union[Unset, str]): The provider of the resource. Example: aws.
        region (Union[Unset, str]): The region where the resource is located. Region values are specific to each
            provider. Example: us-west-2.
        costs (Union[Unset, list['ResourceCost']]): The cost of the resource broken down by category.
        created_at (Union[Unset, str]): The date and time when Vantage first observed the resource.
    """

    token: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    metadata: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    billing_account_id: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    costs: Union[Unset, list["ResourceCost"]] = UNSET
    created_at: Union[Unset, str] = UNSET
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

        costs: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.resource_cost import ResourceCost

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        uuid = d.pop("uuid", UNSET)

        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        metadata = d.pop("metadata", UNSET)

        account_id = d.pop("account_id", UNSET)

        billing_account_id = d.pop("billing_account_id", UNSET)

        provider = d.pop("provider", UNSET)

        region = d.pop("region", UNSET)

        costs = []
        _costs = d.pop("costs", UNSET)
        for costs_item_data in _costs or []:
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
