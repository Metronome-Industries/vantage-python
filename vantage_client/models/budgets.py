from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget import Budget
    from ..models.links import Links


T = TypeVar("T", bound="Budgets")


@_attrs_define
class Budgets:
    """Budgets model

    Attributes:
        links (Union[Unset, Links]):
        budgets (Union[Unset, list['Budget']]):
    """

    links: Union[Unset, "Links"] = UNSET
    budgets: Union[Unset, list["Budget"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        budgets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.budgets, Unset):
            budgets = []
            for budgets_item_data in self.budgets:
                budgets_item = budgets_item_data.to_dict()
                budgets.append(budgets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if budgets is not UNSET:
            field_dict["budgets"] = budgets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.budget import Budget
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        budgets = []
        _budgets = d.pop("budgets", UNSET)
        for budgets_item_data in _budgets or []:
            budgets_item = Budget.from_dict(budgets_item_data)

            budgets.append(budgets_item)

        budgets = cls(
            links=links,
            budgets=budgets,
        )

        budgets.additional_properties = d
        return budgets

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
