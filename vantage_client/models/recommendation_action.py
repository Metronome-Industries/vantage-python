from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendationAction")


@_attrs_define
class RecommendationAction:
    """
    Attributes:
        action (Union[Unset, str]):
        description (Union[Unset, str]):
        potential_savings (Union[Unset, str]): Potential savings in dollars Example: 100.00.
        instance_type (Union[Unset, str]):
        containers (Union[Unset, str]):
        remediation_cli_command (Union[Unset, str]): CLI command to remediate this recommendation Example: aws ec2 stop-
            instances --instance-ids i-1234567890abcdef0.
    """

    action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    potential_savings: Union[Unset, str] = UNSET
    instance_type: Union[Unset, str] = UNSET
    containers: Union[Unset, str] = UNSET
    remediation_cli_command: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        description = self.description

        potential_savings = self.potential_savings

        instance_type = self.instance_type

        containers = self.containers

        remediation_cli_command = self.remediation_cli_command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if potential_savings is not UNSET:
            field_dict["potential_savings"] = potential_savings
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if containers is not UNSET:
            field_dict["containers"] = containers
        if remediation_cli_command is not UNSET:
            field_dict["remediation_cli_command"] = remediation_cli_command

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        description = d.pop("description", UNSET)

        potential_savings = d.pop("potential_savings", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        containers = d.pop("containers", UNSET)

        remediation_cli_command = d.pop("remediation_cli_command", UNSET)

        recommendation_action = cls(
            action=action,
            description=description,
            potential_savings=potential_savings,
            instance_type=instance_type,
            containers=containers,
            remediation_cli_command=remediation_cli_command,
        )

        recommendation_action.additional_properties = d
        return recommendation_action

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
