from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cost_provider import CostProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_usage import CostUsage
    from ..models.links import Links


T = TypeVar("T", bound="Cost")


@_attrs_define
class Cost:
    """Cost model

    Attributes:
        links (Union[Unset, Links]):
        accrued_at (Union[Unset, str]): The date the cost was accrued. ISO 8601 Formatted. Example: 2023-09-05+00:00.
        amount (Union[Unset, str]): The amount of the cost. Example: 4.25.
        currency (Union[Unset, str]): The currency of the cost. Example: USD.
        usage (Union[Unset, CostUsage]): The usage amount and unit incurred by the cost.
        provider (Union[Unset, CostProvider]): The cost provider which incurred the cost. Example: aws.
        billing_account_id (Union[Unset, str]): The cost provider's billing account id that incurred the cost. Example:
            9109237192.
        account_id (Union[Unset, str]): The cost provider's account id that incurred the cost. Example: 9109237192.
        service (Union[Unset, str]): The service which incurred the cost. Example: Amazon Elastic Compute Cloud -
            Compute.
        region (Union[Unset, str]): The region which incurred the cost. Example: us-east-1.
        resource_id (Union[Unset, str]): The resource id which incurred the cost. Example: arn:aws:ec2:us-
            east-1:123456789012:instance/i-1234567890abcdef0.
        tag (Union[Unset, str]): The tag attached to the cost that was incurred.
            DEPRECATED: does not support multiple tags. Example: production.
        tags (Union[Unset, list[str]]): The tag pairs attached to the cost that was incurred.
        cost_category (Union[Unset, str]): The category for the cost. Example: Data Transfer.
        cost_subcategory (Union[Unset, str]): The subcategory for the cost. Example: DataTransfer-Regional-Bytes.
    """

    links: Union[Unset, "Links"] = UNSET
    accrued_at: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    usage: Union[Unset, "CostUsage"] = UNSET
    provider: Union[Unset, CostProvider] = UNSET
    billing_account_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    resource_id: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    cost_category: Union[Unset, str] = UNSET
    cost_subcategory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        accrued_at = self.accrued_at

        amount = self.amount

        currency = self.currency

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        billing_account_id = self.billing_account_id

        account_id = self.account_id

        service = self.service

        region = self.region

        resource_id = self.resource_id

        tag = self.tag

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        cost_category = self.cost_category

        cost_subcategory = self.cost_subcategory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if accrued_at is not UNSET:
            field_dict["accrued_at"] = accrued_at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if usage is not UNSET:
            field_dict["usage"] = usage
        if provider is not UNSET:
            field_dict["provider"] = provider
        if billing_account_id is not UNSET:
            field_dict["billing_account_id"] = billing_account_id
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if service is not UNSET:
            field_dict["service"] = service
        if region is not UNSET:
            field_dict["region"] = region
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tags is not UNSET:
            field_dict["tags"] = tags
        if cost_category is not UNSET:
            field_dict["cost_category"] = cost_category
        if cost_subcategory is not UNSET:
            field_dict["cost_subcategory"] = cost_subcategory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cost_usage import CostUsage
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        accrued_at = d.pop("accrued_at", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, CostUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = CostUsage.from_dict(_usage)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CostProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CostProvider(_provider)

        billing_account_id = d.pop("billing_account_id", UNSET)

        account_id = d.pop("account_id", UNSET)

        service = d.pop("service", UNSET)

        region = d.pop("region", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        tag = d.pop("tag", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        cost_category = d.pop("cost_category", UNSET)

        cost_subcategory = d.pop("cost_subcategory", UNSET)

        cost = cls(
            links=links,
            accrued_at=accrued_at,
            amount=amount,
            currency=currency,
            usage=usage,
            provider=provider,
            billing_account_id=billing_account_id,
            account_id=account_id,
            service=service,
            region=region,
            resource_id=resource_id,
            tag=tag,
            tags=tags,
            cost_category=cost_category,
            cost_subcategory=cost_subcategory,
        )

        cost.additional_properties = d
        return cost

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
