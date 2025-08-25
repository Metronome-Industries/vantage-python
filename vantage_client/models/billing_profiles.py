from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_profile import BillingProfile
    from ..models.billing_profiles_links import BillingProfilesLinks


T = TypeVar("T", bound="BillingProfiles")


@_attrs_define
class BillingProfiles:
    """BillingProfiles model

    Attributes:
        links (Union[Unset, BillingProfilesLinks]):
        billing_profiles (Union[Unset, list['BillingProfile']]):
    """

    links: Union[Unset, "BillingProfilesLinks"] = UNSET
    billing_profiles: Union[Unset, list["BillingProfile"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        billing_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_profiles, Unset):
            billing_profiles = []
            for billing_profiles_item_data in self.billing_profiles:
                billing_profiles_item = billing_profiles_item_data.to_dict()
                billing_profiles.append(billing_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if billing_profiles is not UNSET:
            field_dict["billing_profiles"] = billing_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_profile import BillingProfile
        from ..models.billing_profiles_links import BillingProfilesLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, BillingProfilesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BillingProfilesLinks.from_dict(_links)

        billing_profiles = []
        _billing_profiles = d.pop("billing_profiles", UNSET)
        for billing_profiles_item_data in _billing_profiles or []:
            billing_profiles_item = BillingProfile.from_dict(billing_profiles_item_data)

            billing_profiles.append(billing_profiles_item)

        billing_profiles = cls(
            links=links,
            billing_profiles=billing_profiles,
        )

        billing_profiles.additional_properties = d
        return billing_profiles

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
