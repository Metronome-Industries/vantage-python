from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.user_costs_upload import UserCostsUpload


T = TypeVar("T", bound="UserCostsUploads")


@_attrs_define
class UserCostsUploads:
    """UserCostsUploads model

    Attributes:
        links (Union[Unset, Links]):
        user_costs_uploads (Union[Unset, list['UserCostsUpload']]):
    """

    links: Union[Unset, "Links"] = UNSET
    user_costs_uploads: Union[Unset, list["UserCostsUpload"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        user_costs_uploads: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.user_costs_upload import UserCostsUpload

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        user_costs_uploads = []
        _user_costs_uploads = d.pop("user_costs_uploads", UNSET)
        for user_costs_uploads_item_data in _user_costs_uploads or []:
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
