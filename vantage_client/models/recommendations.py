from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recommendation import Recommendation
    from ..models.recommendations_links import RecommendationsLinks


T = TypeVar("T", bound="Recommendations")


@_attrs_define
class Recommendations:
    """Recommendations model

    Attributes:
        links (RecommendationsLinks | Unset):
        recommendations (list[Recommendation] | Unset):
    """

    links: RecommendationsLinks | Unset = UNSET
    recommendations: list[Recommendation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        recommendations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommendations, Unset):
            recommendations = []
            for recommendations_item_data in self.recommendations:
                recommendations_item = recommendations_item_data.to_dict()
                recommendations.append(recommendations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if recommendations is not UNSET:
            field_dict["recommendations"] = recommendations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommendation import Recommendation
        from ..models.recommendations_links import RecommendationsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: RecommendationsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RecommendationsLinks.from_dict(_links)

        _recommendations = d.pop("recommendations", UNSET)
        recommendations: list[Recommendation] | Unset = UNSET
        if _recommendations is not UNSET:
            recommendations = []
            for recommendations_item_data in _recommendations:
                recommendations_item = Recommendation.from_dict(recommendations_item_data)

                recommendations.append(recommendations_item)

        recommendations = cls(
            links=links,
            recommendations=recommendations,
        )

        recommendations.additional_properties = d
        return recommendations

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
