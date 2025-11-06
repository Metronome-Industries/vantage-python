from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bearer_token import BearerToken
    from ..models.workspace import Workspace


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """Me model

    Attributes:
        default_workspace_token (str | Unset):
        workspaces (list[Workspace] | Unset):
        bearer_token (BearerToken | Unset):
    """

    default_workspace_token: str | Unset = UNSET
    workspaces: list[Workspace] | Unset = UNSET
    bearer_token: BearerToken | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_workspace_token = self.default_workspace_token

        workspaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workspaces, Unset):
            workspaces = []
            for workspaces_item_data in self.workspaces:
                workspaces_item = workspaces_item_data.to_dict()
                workspaces.append(workspaces_item)

        bearer_token: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bearer_token, Unset):
            bearer_token = self.bearer_token.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_workspace_token is not UNSET:
            field_dict["default_workspace_token"] = default_workspace_token
        if workspaces is not UNSET:
            field_dict["workspaces"] = workspaces
        if bearer_token is not UNSET:
            field_dict["bearer_token"] = bearer_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bearer_token import BearerToken
        from ..models.workspace import Workspace

        d = dict(src_dict)
        default_workspace_token = d.pop("default_workspace_token", UNSET)

        _workspaces = d.pop("workspaces", UNSET)
        workspaces: list[Workspace] | Unset = UNSET
        if _workspaces is not UNSET:
            workspaces = []
            for workspaces_item_data in _workspaces:
                workspaces_item = Workspace.from_dict(workspaces_item_data)

                workspaces.append(workspaces_item)

        _bearer_token = d.pop("bearer_token", UNSET)
        bearer_token: BearerToken | Unset
        if isinstance(_bearer_token, Unset):
            bearer_token = UNSET
        else:
            bearer_token = BearerToken.from_dict(_bearer_token)

        me = cls(
            default_workspace_token=default_workspace_token,
            workspaces=workspaces,
            bearer_token=bearer_token,
        )

        me.additional_properties = d
        return me

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
