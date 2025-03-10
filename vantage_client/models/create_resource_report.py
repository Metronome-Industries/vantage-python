from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResourceReport")


@_attrs_define
class CreateResourceReport:
    """Create a ResourceReport.

    Attributes:
        workspace_token (str): The token of the Workspace to add the ResourceReport to.
        title (Union[Unset, str]): The title of the ResourceReport.
        filter_ (Union[Unset, str]): The filter query language to apply to the ResourceReport. Additional documentation
            available at https://docs.vantage.sh/vql.
    """

    workspace_token: str
    title: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_token = self.workspace_token

        title = self.title

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_token": workspace_token,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_token = d.pop("workspace_token")

        title = d.pop("title", UNSET)

        filter_ = d.pop("filter", UNSET)

        create_resource_report = cls(
            workspace_token=workspace_token,
            title=title,
            filter_=filter_,
        )

        create_resource_report.additional_properties = d
        return create_resource_report

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
