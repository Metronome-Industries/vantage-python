import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_network_flow_report_date_interval import CreateNetworkFlowReportDateInterval
from ..models.create_network_flow_report_flow_direction import CreateNetworkFlowReportFlowDirection
from ..models.create_network_flow_report_flow_weight import CreateNetworkFlowReportFlowWeight
from ..models.create_network_flow_report_groupings_item import CreateNetworkFlowReportGroupingsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNetworkFlowReport")


@_attrs_define
class CreateNetworkFlowReport:
    """Create a NetworkFlowReport.

    Attributes:
        workspace_token (str): The Workspace in which the NetworkFlowReport will be created.
        title (str): The title of the NetworkFlowReport.
        filter_ (Union[Unset, str]): The filter query language to apply to the NetworkFlowReport. Additional
            documentation available at https://docs.vantage.sh/vql.
        start_date (Union[Unset, datetime.date]): The start date of the NetworkFlowReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter.
        end_date (Union[Unset, datetime.date]): The end date of the NetworkFlowReport. YYYY-MM-DD formatted.
            Incompatible with 'date_interval' parameter.
        date_interval (Union[Unset, CreateNetworkFlowReportDateInterval]): The date interval of the NetworkFlowReport.
            Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date' parameters. Defaults to
            'last_7_days'.
        groupings (Union[Unset, list[CreateNetworkFlowReportGroupingsItem]]): Grouping values for aggregating data on
            the NetworkFlowReport. Valid groupings: account_id, az_id, dstaddr, dsthostname, flow_direction, interface_id,
            instance_id, peer_resource_uuid, peer_account_id, peer_vpc_id, peer_region, peer_az_id, peer_subnet_id,
            peer_interface_id, peer_instance_id, region, resource_uuid, srcaddr, srchostname, subnet_id, traffic_category,
            traffic_path, vpc_id.
        flow_direction (Union[Unset, CreateNetworkFlowReportFlowDirection]): The flow direction of the
            NetworkFlowReport.
        flow_weight (Union[Unset, CreateNetworkFlowReportFlowWeight]): The dimension by which the logs in the report are
            sorted. Defaults to costs.
    """

    workspace_token: str
    title: str
    filter_: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    date_interval: Union[Unset, CreateNetworkFlowReportDateInterval] = UNSET
    groupings: Union[Unset, list[CreateNetworkFlowReportGroupingsItem]] = UNSET
    flow_direction: Union[Unset, CreateNetworkFlowReportFlowDirection] = UNSET
    flow_weight: Union[Unset, CreateNetworkFlowReportFlowWeight] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_token = self.workspace_token

        title = self.title

        filter_ = self.filter_

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        date_interval: Union[Unset, str] = UNSET
        if not isinstance(self.date_interval, Unset):
            date_interval = self.date_interval.value

        groupings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groupings, Unset):
            groupings = []
            for groupings_item_data in self.groupings:
                groupings_item = groupings_item_data.value
                groupings.append(groupings_item)

        flow_direction: Union[Unset, str] = UNSET
        if not isinstance(self.flow_direction, Unset):
            flow_direction = self.flow_direction.value

        flow_weight: Union[Unset, str] = UNSET
        if not isinstance(self.flow_weight, Unset):
            flow_weight = self.flow_weight.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_token": workspace_token,
                "title": title,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if date_interval is not UNSET:
            field_dict["date_interval"] = date_interval
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if flow_direction is not UNSET:
            field_dict["flow_direction"] = flow_direction
        if flow_weight is not UNSET:
            field_dict["flow_weight"] = flow_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_token = d.pop("workspace_token")

        title = d.pop("title")

        filter_ = d.pop("filter", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _date_interval = d.pop("date_interval", UNSET)
        date_interval: Union[Unset, CreateNetworkFlowReportDateInterval]
        if isinstance(_date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = CreateNetworkFlowReportDateInterval(_date_interval)

        groupings = []
        _groupings = d.pop("groupings", UNSET)
        for groupings_item_data in _groupings or []:
            groupings_item = CreateNetworkFlowReportGroupingsItem(groupings_item_data)

            groupings.append(groupings_item)

        _flow_direction = d.pop("flow_direction", UNSET)
        flow_direction: Union[Unset, CreateNetworkFlowReportFlowDirection]
        if isinstance(_flow_direction, Unset):
            flow_direction = UNSET
        else:
            flow_direction = CreateNetworkFlowReportFlowDirection(_flow_direction)

        _flow_weight = d.pop("flow_weight", UNSET)
        flow_weight: Union[Unset, CreateNetworkFlowReportFlowWeight]
        if isinstance(_flow_weight, Unset):
            flow_weight = UNSET
        else:
            flow_weight = CreateNetworkFlowReportFlowWeight(_flow_weight)

        create_network_flow_report = cls(
            workspace_token=workspace_token,
            title=title,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
            date_interval=date_interval,
            groupings=groupings,
            flow_direction=flow_direction,
            flow_weight=flow_weight,
        )

        create_network_flow_report.additional_properties = d
        return create_network_flow_report

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
