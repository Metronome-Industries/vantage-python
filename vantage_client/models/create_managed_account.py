from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateManagedAccount")


@_attrs_define
class CreateManagedAccount:
    """Create a Managed Account.

    Attributes:
        name (str): The name of the Managed Account.
        contact_email (str): The contact email address for the Managed Account.
        access_credential_tokens (Union[Unset, list[str]]): Access Credential (aka Integrations) tokens to assign to the
            Managed Account.
        billing_rule_tokens (Union[Unset, list[str]]): Billing Rule tokens to assign to the Managed Account.
    """

    name: str
    contact_email: str
    access_credential_tokens: Union[Unset, list[str]] = UNSET
    billing_rule_tokens: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contact_email = self.contact_email

        access_credential_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.access_credential_tokens, Unset):
            access_credential_tokens = self.access_credential_tokens

        billing_rule_tokens: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_rule_tokens, Unset):
            billing_rule_tokens = self.billing_rule_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "contact_email": contact_email,
            }
        )
        if access_credential_tokens is not UNSET:
            field_dict["access_credential_tokens"] = access_credential_tokens
        if billing_rule_tokens is not UNSET:
            field_dict["billing_rule_tokens"] = billing_rule_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        contact_email = d.pop("contact_email")

        access_credential_tokens = cast(list[str], d.pop("access_credential_tokens", UNSET))

        billing_rule_tokens = cast(list[str], d.pop("billing_rule_tokens", UNSET))

        create_managed_account = cls(
            name=name,
            contact_email=contact_email,
            access_credential_tokens=access_credential_tokens,
            billing_rule_tokens=billing_rule_tokens,
        )

        create_managed_account.additional_properties = d
        return create_managed_account

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
