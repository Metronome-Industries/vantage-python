from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_provider_account import CostProviderAccount
    from ..models.cost_provider_accounts_links import CostProviderAccountsLinks


T = TypeVar("T", bound="CostProviderAccounts")


@_attrs_define
class CostProviderAccounts:
    """CostProviderAccounts model

    Attributes:
        links (CostProviderAccountsLinks | Unset):
        cost_provider_accounts (list[CostProviderAccount] | Unset):
    """

    links: CostProviderAccountsLinks | Unset = UNSET
    cost_provider_accounts: list[CostProviderAccount] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        cost_provider_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cost_provider_accounts, Unset):
            cost_provider_accounts = []
            for cost_provider_accounts_item_data in self.cost_provider_accounts:
                cost_provider_accounts_item = cost_provider_accounts_item_data.to_dict()
                cost_provider_accounts.append(cost_provider_accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if cost_provider_accounts is not UNSET:
            field_dict["cost_provider_accounts"] = cost_provider_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_provider_account import CostProviderAccount
        from ..models.cost_provider_accounts_links import CostProviderAccountsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: CostProviderAccountsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CostProviderAccountsLinks.from_dict(_links)

        _cost_provider_accounts = d.pop("cost_provider_accounts", UNSET)
        cost_provider_accounts: list[CostProviderAccount] | Unset = UNSET
        if _cost_provider_accounts is not UNSET:
            cost_provider_accounts = []
            for cost_provider_accounts_item_data in _cost_provider_accounts:
                cost_provider_accounts_item = CostProviderAccount.from_dict(cost_provider_accounts_item_data)

                cost_provider_accounts.append(cost_provider_accounts_item)

        cost_provider_accounts = cls(
            links=links,
            cost_provider_accounts=cost_provider_accounts,
        )

        cost_provider_accounts.additional_properties = d
        return cost_provider_accounts

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
