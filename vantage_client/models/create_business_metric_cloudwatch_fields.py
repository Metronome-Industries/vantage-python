from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_business_metric_cloudwatch_fields_dimensions_item import (
        CreateBusinessMetricCloudwatchFieldsDimensionsItem,
    )


T = TypeVar("T", bound="CreateBusinessMetricCloudwatchFields")


@_attrs_define
class CreateBusinessMetricCloudwatchFields:
    """Cloudwatch configuration fields.

    Attributes:
        integration_token (Union[Unset, str]): Integration token for the account from which you would like to fetch
            metrics.
        stat (Union[Unset, str]):
        region (Union[Unset, str]):
        namespace (Union[Unset, str]):
        metric_name (Union[Unset, str]):
        label_dimension (Union[Unset, str]):
        dimensions (Union[Unset, list['CreateBusinessMetricCloudwatchFieldsDimensionsItem']]):
    """

    integration_token: Union[Unset, str] = UNSET
    stat: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    metric_name: Union[Unset, str] = UNSET
    label_dimension: Union[Unset, str] = UNSET
    dimensions: Union[Unset, list["CreateBusinessMetricCloudwatchFieldsDimensionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_token = self.integration_token

        stat = self.stat

        region = self.region

        namespace = self.namespace

        metric_name = self.metric_name

        label_dimension = self.label_dimension

        dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration_token is not UNSET:
            field_dict["integration_token"] = integration_token
        if stat is not UNSET:
            field_dict["stat"] = stat
        if region is not UNSET:
            field_dict["region"] = region
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if metric_name is not UNSET:
            field_dict["metric_name"] = metric_name
        if label_dimension is not UNSET:
            field_dict["label_dimension"] = label_dimension
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_business_metric_cloudwatch_fields_dimensions_item import (
            CreateBusinessMetricCloudwatchFieldsDimensionsItem,
        )

        d = dict(src_dict)
        integration_token = d.pop("integration_token", UNSET)

        stat = d.pop("stat", UNSET)

        region = d.pop("region", UNSET)

        namespace = d.pop("namespace", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        label_dimension = d.pop("label_dimension", UNSET)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for dimensions_item_data in _dimensions or []:
            dimensions_item = CreateBusinessMetricCloudwatchFieldsDimensionsItem.from_dict(dimensions_item_data)

            dimensions.append(dimensions_item)

        create_business_metric_cloudwatch_fields = cls(
            integration_token=integration_token,
            stat=stat,
            region=region,
            namespace=namespace,
            metric_name=metric_name,
            label_dimension=label_dimension,
            dimensions=dimensions,
        )

        create_business_metric_cloudwatch_fields.additional_properties = d
        return create_business_metric_cloudwatch_fields

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
