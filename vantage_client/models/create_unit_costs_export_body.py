from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_unit_costs_export_body_date_bin import CreateUnitCostsExportBodyDateBin
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUnitCostsExportBody")


@_attrs_define
class CreateUnitCostsExportBody:
    """
    Attributes:
        cost_report_token (str): The CostReport token.
        workspace_token (str | Unset): The token of the Workspace to query costs from. Required if the API token is
            associated with multiple Workspaces.
        start_date (str | Unset): First date you would like to filter unit costs from. Defaults to the report's default.
            ISO 8601 formatted.
        end_date (str | Unset): Last date you would like to filter unit costs to. Defaults to the report's default. ISO
            8601 formatted.
        date_bin (CreateUnitCostsExportBodyDateBin | Unset): The date bin of the unit costs. Defaults to the report's
            default or day.
    """

    cost_report_token: str
    workspace_token: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    date_bin: CreateUnitCostsExportBodyDateBin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_report_token = self.cost_report_token

        workspace_token = self.workspace_token

        start_date = self.start_date

        end_date = self.end_date

        date_bin: str | Unset = UNSET
        if not isinstance(self.date_bin, Unset):
            date_bin = self.date_bin.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_report_token": cost_report_token,
            }
        )
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_bin is not UNSET:
            field_dict["date_bin"] = date_bin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_report_token = d.pop("cost_report_token")

        workspace_token = d.pop("workspace_token", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        _date_bin = d.pop("date_bin", UNSET)
        date_bin: CreateUnitCostsExportBodyDateBin | Unset
        if isinstance(_date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = CreateUnitCostsExportBodyDateBin(_date_bin)

        create_unit_costs_export_body = cls(
            cost_report_token=cost_report_token,
            workspace_token=workspace_token,
            start_date=start_date,
            end_date=end_date,
            date_bin=date_bin,
        )

        create_unit_costs_export_body.additional_properties = d
        return create_unit_costs_export_body

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
