from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_cost_report_for_business_metric import AttachedCostReportForBusinessMetric


T = TypeVar("T", bound="BusinessMetric")


@_attrs_define
class BusinessMetric:
    """BusinessMetric model

    Attributes:
        token (Union[Unset, str]): The token of the BusinessMetric. Example: bsnss_mtrc_1234.
        title (Union[Unset, str]): The title of the BusinessMetric. Example: Total Revenue.
        created_by_token (Union[Unset, str]): The token of the Creator of the BusinessMetric. Example: usr_1234.
        cost_report_tokens_with_metadata (Union[Unset, list['AttachedCostReportForBusinessMetric']]): The tokens for any
            CostReports that use the BusinessMetric, the unit scale, and label filter.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    cost_report_tokens_with_metadata: Union[Unset, list["AttachedCostReportForBusinessMetric"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        created_by_token = self.created_by_token

        cost_report_tokens_with_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cost_report_tokens_with_metadata, Unset):
            cost_report_tokens_with_metadata = []
            for cost_report_tokens_with_metadata_item_data in self.cost_report_tokens_with_metadata:
                cost_report_tokens_with_metadata_item = cost_report_tokens_with_metadata_item_data.to_dict()
                cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if cost_report_tokens_with_metadata is not UNSET:
            field_dict["cost_report_tokens_with_metadata"] = cost_report_tokens_with_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attached_cost_report_for_business_metric import AttachedCostReportForBusinessMetric

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        cost_report_tokens_with_metadata = []
        _cost_report_tokens_with_metadata = d.pop("cost_report_tokens_with_metadata", UNSET)
        for cost_report_tokens_with_metadata_item_data in _cost_report_tokens_with_metadata or []:
            cost_report_tokens_with_metadata_item = AttachedCostReportForBusinessMetric.from_dict(
                cost_report_tokens_with_metadata_item_data
            )

            cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        business_metric = cls(
            token=token,
            title=title,
            created_by_token=created_by_token,
            cost_report_tokens_with_metadata=cost_report_tokens_with_metadata,
        )

        business_metric.additional_properties = d
        return business_metric

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
