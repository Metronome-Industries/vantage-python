from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_business_metric_cost_report_tokens_with_metadata_item_unit_scale import (
    UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBusinessMetricCostReportTokensWithMetadataItem")


@_attrs_define
class UpdateBusinessMetricCostReportTokensWithMetadataItem:
    """
    Attributes:
        cost_report_token (str): The token of the CostReport the BusinessMetric is attached to.
        unit_scale (Union[Unset, UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale]): Determines the scale
            of the BusinessMetric's values within the CostReport. Default:
            UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale.PER_UNIT.
        label_filter (Union[Unset, list[str]]): Include only values with these labels in the CostReport.
    """

    cost_report_token: str
    unit_scale: Union[Unset, UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale] = (
        UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale.PER_UNIT
    )
    label_filter: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_report_token = self.cost_report_token

        unit_scale: Union[Unset, str] = UNSET
        if not isinstance(self.unit_scale, Unset):
            unit_scale = self.unit_scale.value

        label_filter: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_filter, Unset):
            label_filter = self.label_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_report_token": cost_report_token,
            }
        )
        if unit_scale is not UNSET:
            field_dict["unit_scale"] = unit_scale
        if label_filter is not UNSET:
            field_dict["label_filter"] = label_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_report_token = d.pop("cost_report_token")

        _unit_scale = d.pop("unit_scale", UNSET)
        unit_scale: Union[Unset, UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale]
        if isinstance(_unit_scale, Unset):
            unit_scale = UNSET
        else:
            unit_scale = UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale(_unit_scale)

        label_filter = cast(list[str], d.pop("label_filter", UNSET))

        update_business_metric_cost_report_tokens_with_metadata_item = cls(
            cost_report_token=cost_report_token,
            unit_scale=unit_scale,
            label_filter=label_filter,
        )

        update_business_metric_cost_report_tokens_with_metadata_item.additional_properties = d
        return update_business_metric_cost_report_tokens_with_metadata_item

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
