from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.banking_information import BankingInformation
    from ..models.billing_information import BillingInformation
    from ..models.business_information import BusinessInformation


T = TypeVar("T", bound="BillingProfile")


@_attrs_define
class BillingProfile:
    """BillingProfile model

    Attributes:
        id (Union[Unset, str]):
        token (Union[Unset, str]):
        nickname (Union[Unset, str]): Display name for the billing profile
        created_at (Union[Unset, str]): The date and time, in UTC, the billing profile was created. ISO 8601 formatted.
            Example: 2023-08-04T00:00:00Z.
        updated_at (Union[Unset, str]): The date and time, in UTC, the billing profile was last updated. ISO 8601
            formatted. Example: 2023-08-04T00:00:00Z.
        billing_information_attributes (Union[Unset, BillingInformation]):
        business_information_attributes (Union[Unset, BusinessInformation]):
        banking_information_attributes (Union[Unset, BankingInformation]):
        managed_accounts_count (Union[Unset, str]): Number of managed accounts using this billing profile
    """

    id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    billing_information_attributes: Union[Unset, "BillingInformation"] = UNSET
    business_information_attributes: Union[Unset, "BusinessInformation"] = UNSET
    banking_information_attributes: Union[Unset, "BankingInformation"] = UNSET
    managed_accounts_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        nickname = self.nickname

        created_at = self.created_at

        updated_at = self.updated_at

        billing_information_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_information_attributes, Unset):
            billing_information_attributes = self.billing_information_attributes.to_dict()

        business_information_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business_information_attributes, Unset):
            business_information_attributes = self.business_information_attributes.to_dict()

        banking_information_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.banking_information_attributes, Unset):
            banking_information_attributes = self.banking_information_attributes.to_dict()

        managed_accounts_count = self.managed_accounts_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if billing_information_attributes is not UNSET:
            field_dict["billing_information_attributes"] = billing_information_attributes
        if business_information_attributes is not UNSET:
            field_dict["business_information_attributes"] = business_information_attributes
        if banking_information_attributes is not UNSET:
            field_dict["banking_information_attributes"] = banking_information_attributes
        if managed_accounts_count is not UNSET:
            field_dict["managed_accounts_count"] = managed_accounts_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banking_information import BankingInformation
        from ..models.billing_information import BillingInformation
        from ..models.business_information import BusinessInformation

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        nickname = d.pop("nickname", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _billing_information_attributes = d.pop("billing_information_attributes", UNSET)
        billing_information_attributes: Union[Unset, BillingInformation]
        if isinstance(_billing_information_attributes, Unset):
            billing_information_attributes = UNSET
        else:
            billing_information_attributes = BillingInformation.from_dict(_billing_information_attributes)

        _business_information_attributes = d.pop("business_information_attributes", UNSET)
        business_information_attributes: Union[Unset, BusinessInformation]
        if isinstance(_business_information_attributes, Unset):
            business_information_attributes = UNSET
        else:
            business_information_attributes = BusinessInformation.from_dict(_business_information_attributes)

        _banking_information_attributes = d.pop("banking_information_attributes", UNSET)
        banking_information_attributes: Union[Unset, BankingInformation]
        if isinstance(_banking_information_attributes, Unset):
            banking_information_attributes = UNSET
        else:
            banking_information_attributes = BankingInformation.from_dict(_banking_information_attributes)

        managed_accounts_count = d.pop("managed_accounts_count", UNSET)

        billing_profile = cls(
            id=id,
            token=token,
            nickname=nickname,
            created_at=created_at,
            updated_at=updated_at,
            billing_information_attributes=billing_information_attributes,
            business_information_attributes=business_information_attributes,
            banking_information_attributes=banking_information_attributes,
            managed_accounts_count=managed_accounts_count,
        )

        billing_profile.additional_properties = d
        return billing_profile

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
