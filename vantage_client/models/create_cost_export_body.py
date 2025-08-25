from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_cost_export_body_date_bin import CreateCostExportBodyDateBin
from ..models.create_cost_export_body_schema import CreateCostExportBodySchema
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCostExportBody")


@_attrs_define
class CreateCostExportBody:
    """
    Attributes:
        cost_report_token (Union[Unset, str]): The CostReport token.
        filter_ (Union[Unset, str]): The VQL filter to apply to the costs. If this is supplied you do not need
            cost_report_token.
        workspace_token (Union[Unset, str]): The token of the Workspace to query costs from. Ignored if
            'cost_report_token' is set. Required if the API token is associated with multiple Workspaces.
        start_date (Union[Unset, str]): First date you would like to filter costs from. ISO 8601 formatted.
        end_date (Union[Unset, str]): Last date you would like to filter costs to. ISO 8601 formatted.
        date_bin (Union[Unset, CreateCostExportBodyDateBin]): The date bin of the costs. Defaults to the report's
            default or day.
        schema (Union[Unset, CreateCostExportBodySchema]): The schema of the data export. Default:
            CreateCostExportBodySchema.VNTG.
        settingsinclude_credits (Union[Unset, bool]): Results will include credits. Default: False.
        settingsinclude_refunds (Union[Unset, bool]): Results will include refunds. Default: False.
        settingsinclude_discounts (Union[Unset, bool]): Results will include discounts. Default: True.
        settingsinclude_tax (Union[Unset, bool]): Results will include tax. Default: True.
        settingsamortize (Union[Unset, bool]): Results will amortize. Default: True.
        settingsunallocated (Union[Unset, bool]): Results will show unallocated costs. Default: False.
        settingsaggregate_by (Union[Unset, str]): Results will aggregate by cost or usage. Default: 'cost'.
        settingsshow_previous_period (Union[Unset, bool]): Results will show previous period costs or usage comparison.
            Default: True.
    """

    cost_report_token: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    date_bin: Union[Unset, CreateCostExportBodyDateBin] = UNSET
    schema: Union[Unset, CreateCostExportBodySchema] = CreateCostExportBodySchema.VNTG
    settingsinclude_credits: Union[Unset, bool] = False
    settingsinclude_refunds: Union[Unset, bool] = False
    settingsinclude_discounts: Union[Unset, bool] = True
    settingsinclude_tax: Union[Unset, bool] = True
    settingsamortize: Union[Unset, bool] = True
    settingsunallocated: Union[Unset, bool] = False
    settingsaggregate_by: Union[Unset, str] = "cost"
    settingsshow_previous_period: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_report_token = self.cost_report_token

        filter_ = self.filter_

        workspace_token = self.workspace_token

        start_date = self.start_date

        end_date = self.end_date

        date_bin: Union[Unset, str] = UNSET
        if not isinstance(self.date_bin, Unset):
            date_bin = self.date_bin.value

        schema: Union[Unset, str] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.value

        settingsinclude_credits = self.settingsinclude_credits

        settingsinclude_refunds = self.settingsinclude_refunds

        settingsinclude_discounts = self.settingsinclude_discounts

        settingsinclude_tax = self.settingsinclude_tax

        settingsamortize = self.settingsamortize

        settingsunallocated = self.settingsunallocated

        settingsaggregate_by = self.settingsaggregate_by

        settingsshow_previous_period = self.settingsshow_previous_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_bin is not UNSET:
            field_dict["date_bin"] = date_bin
        if schema is not UNSET:
            field_dict["schema"] = schema
        if settingsinclude_credits is not UNSET:
            field_dict["settings[include_credits]"] = settingsinclude_credits
        if settingsinclude_refunds is not UNSET:
            field_dict["settings[include_refunds]"] = settingsinclude_refunds
        if settingsinclude_discounts is not UNSET:
            field_dict["settings[include_discounts]"] = settingsinclude_discounts
        if settingsinclude_tax is not UNSET:
            field_dict["settings[include_tax]"] = settingsinclude_tax
        if settingsamortize is not UNSET:
            field_dict["settings[amortize]"] = settingsamortize
        if settingsunallocated is not UNSET:
            field_dict["settings[unallocated]"] = settingsunallocated
        if settingsaggregate_by is not UNSET:
            field_dict["settings[aggregate_by]"] = settingsaggregate_by
        if settingsshow_previous_period is not UNSET:
            field_dict["settings[show_previous_period]"] = settingsshow_previous_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_report_token = d.pop("cost_report_token", UNSET)

        filter_ = d.pop("filter", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        _date_bin = d.pop("date_bin", UNSET)
        date_bin: Union[Unset, CreateCostExportBodyDateBin]
        if isinstance(_date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = CreateCostExportBodyDateBin(_date_bin)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, CreateCostExportBodySchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = CreateCostExportBodySchema(_schema)

        settingsinclude_credits = d.pop("settings[include_credits]", UNSET)

        settingsinclude_refunds = d.pop("settings[include_refunds]", UNSET)

        settingsinclude_discounts = d.pop("settings[include_discounts]", UNSET)

        settingsinclude_tax = d.pop("settings[include_tax]", UNSET)

        settingsamortize = d.pop("settings[amortize]", UNSET)

        settingsunallocated = d.pop("settings[unallocated]", UNSET)

        settingsaggregate_by = d.pop("settings[aggregate_by]", UNSET)

        settingsshow_previous_period = d.pop("settings[show_previous_period]", UNSET)

        create_cost_export_body = cls(
            cost_report_token=cost_report_token,
            filter_=filter_,
            workspace_token=workspace_token,
            start_date=start_date,
            end_date=end_date,
            date_bin=date_bin,
            schema=schema,
            settingsinclude_credits=settingsinclude_credits,
            settingsinclude_refunds=settingsinclude_refunds,
            settingsinclude_discounts=settingsinclude_discounts,
            settingsinclude_tax=settingsinclude_tax,
            settingsamortize=settingsamortize,
            settingsunallocated=settingsunallocated,
            settingsaggregate_by=settingsaggregate_by,
            settingsshow_previous_period=settingsshow_previous_period,
        )

        create_cost_export_body.additional_properties = d
        return create_cost_export_body

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
