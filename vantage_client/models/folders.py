from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder import Folder
    from ..models.folders_links import FoldersLinks


T = TypeVar("T", bound="Folders")


@_attrs_define
class Folders:
    """Folders model

    Attributes:
        links (Union[Unset, FoldersLinks]):
        folders (Union[Unset, list['Folder']]):
    """

    links: Union[Unset, "FoldersLinks"] = UNSET
    folders: Union[Unset, list["Folder"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        folders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.folder import Folder
        from ..models.folders_links import FoldersLinks

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, FoldersLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FoldersLinks.from_dict(_links)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = Folder.from_dict(folders_item_data)

            folders.append(folders_item)

        folders = cls(
            links=links,
            folders=folders,
        )

        folders.additional_properties = d
        return folders

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
