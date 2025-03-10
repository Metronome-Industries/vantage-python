from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.managed_account import ManagedAccount


T = TypeVar("T", bound="ManagedAccounts")


@_attrs_define
class ManagedAccounts:
    """ManagedAccounts model

    Attributes:
        links (Union[Unset, Links]):
        managed_accounts (Union[Unset, list['ManagedAccount']]):
    """

    links: Union[Unset, "Links"] = UNSET
    managed_accounts: Union[Unset, list["ManagedAccount"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        managed_accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.managed_accounts, Unset):
            managed_accounts = []
            for managed_accounts_item_data in self.managed_accounts:
                managed_accounts_item = managed_accounts_item_data.to_dict()
                managed_accounts.append(managed_accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if managed_accounts is not UNSET:
            field_dict["managed_accounts"] = managed_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.managed_account import ManagedAccount

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        managed_accounts = []
        _managed_accounts = d.pop("managed_accounts", UNSET)
        for managed_accounts_item_data in _managed_accounts or []:
            managed_accounts_item = ManagedAccount.from_dict(managed_accounts_item_data)

            managed_accounts.append(managed_accounts_item)

        managed_accounts = cls(
            links=links,
            managed_accounts=managed_accounts,
        )

        managed_accounts.additional_properties = d
        return managed_accounts

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
