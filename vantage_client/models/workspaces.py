from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace import Workspace
    from ..models.workspaces_links import WorkspacesLinks


T = TypeVar("T", bound="Workspaces")


@_attrs_define
class Workspaces:
    """Workspaces model

    Attributes:
        links (WorkspacesLinks | Unset):
        workspaces (list[Workspace] | Unset):
    """

    links: WorkspacesLinks | Unset = UNSET
    workspaces: list[Workspace] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        workspaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workspaces, Unset):
            workspaces = []
            for workspaces_item_data in self.workspaces:
                workspaces_item = workspaces_item_data.to_dict()
                workspaces.append(workspaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if workspaces is not UNSET:
            field_dict["workspaces"] = workspaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace import Workspace
        from ..models.workspaces_links import WorkspacesLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: WorkspacesLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkspacesLinks.from_dict(_links)

        _workspaces = d.pop("workspaces", UNSET)
        workspaces: list[Workspace] | Unset = UNSET
        if _workspaces is not UNSET:
            workspaces = []
            for workspaces_item_data in _workspaces:
                workspaces_item = Workspace.from_dict(workspaces_item_data)

                workspaces.append(workspaces_item)

        workspaces = cls(
            links=links,
            workspaces=workspaces,
        )

        workspaces.additional_properties = d
        return workspaces

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
