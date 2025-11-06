from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_costs_upload import UserCostsUpload
    from ..models.user_costs_uploads_links import UserCostsUploadsLinks


T = TypeVar("T", bound="UserCostsUploads")


@_attrs_define
class UserCostsUploads:
    """UserCostsUploads model

    Attributes:
        links (UserCostsUploadsLinks | Unset):
        user_costs_uploads (list[UserCostsUpload] | Unset):
    """

    links: UserCostsUploadsLinks | Unset = UNSET
    user_costs_uploads: list[UserCostsUpload] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        user_costs_uploads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_costs_uploads, Unset):
            user_costs_uploads = []
            for user_costs_uploads_item_data in self.user_costs_uploads:
                user_costs_uploads_item = user_costs_uploads_item_data.to_dict()
                user_costs_uploads.append(user_costs_uploads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if user_costs_uploads is not UNSET:
            field_dict["user_costs_uploads"] = user_costs_uploads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_costs_upload import UserCostsUpload
        from ..models.user_costs_uploads_links import UserCostsUploadsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: UserCostsUploadsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UserCostsUploadsLinks.from_dict(_links)

        _user_costs_uploads = d.pop("user_costs_uploads", UNSET)
        user_costs_uploads: list[UserCostsUpload] | Unset = UNSET
        if _user_costs_uploads is not UNSET:
            user_costs_uploads = []
            for user_costs_uploads_item_data in _user_costs_uploads:
                user_costs_uploads_item = UserCostsUpload.from_dict(user_costs_uploads_item_data)

                user_costs_uploads.append(user_costs_uploads_item)

        user_costs_uploads = cls(
            links=links,
            user_costs_uploads=user_costs_uploads,
        )

        user_costs_uploads.additional_properties = d
        return user_costs_uploads

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
