from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recommendation_action import RecommendationAction


T = TypeVar("T", bound="ProviderResource")


@_attrs_define
class ProviderResource:
    """ProviderResource model

    Attributes:
        token (Union[Unset, str]):
        resource_id (Union[Unset, str]): The unique identifier of the Active Resource. Example: i-0a1b2c3d4e5f6g7h8.
        recommendation_actions (Union[Unset, list['RecommendationAction']]): The actions to take to implement the
            Recommendation.
    """

    token: Union[Unset, str] = UNSET
    resource_id: Union[Unset, str] = UNSET
    recommendation_actions: Union[Unset, list["RecommendationAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        resource_id = self.resource_id

        recommendation_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recommendation_actions, Unset):
            recommendation_actions = []
            for recommendation_actions_item_data in self.recommendation_actions:
                recommendation_actions_item = recommendation_actions_item_data.to_dict()
                recommendation_actions.append(recommendation_actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if recommendation_actions is not UNSET:
            field_dict["recommendation_actions"] = recommendation_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.recommendation_action import RecommendationAction

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        recommendation_actions = []
        _recommendation_actions = d.pop("recommendation_actions", UNSET)
        for recommendation_actions_item_data in _recommendation_actions or []:
            recommendation_actions_item = RecommendationAction.from_dict(recommendation_actions_item_data)

            recommendation_actions.append(recommendation_actions_item)

        provider_resource = cls(
            token=token,
            resource_id=resource_id,
            recommendation_actions=recommendation_actions,
        )

        provider_resource.additional_properties = d
        return provider_resource

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
