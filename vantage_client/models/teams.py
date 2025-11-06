from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team
    from ..models.teams_links import TeamsLinks


T = TypeVar("T", bound="Teams")


@_attrs_define
class Teams:
    """Teams model

    Attributes:
        links (TeamsLinks | Unset):
        teams (list[Team] | Unset):
    """

    links: TeamsLinks | Unset = UNSET
    teams: list[Team] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team import Team
        from ..models.teams_links import TeamsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: TeamsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TeamsLinks.from_dict(_links)

        _teams = d.pop("teams", UNSET)
        teams: list[Team] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = Team.from_dict(teams_item_data)

                teams.append(teams_item)

        teams = cls(
            links=links,
            teams=teams,
        )

        teams.additional_properties = d
        return teams

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
