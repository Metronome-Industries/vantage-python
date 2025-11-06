from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_segment_report_settings import CreateSegmentReportSettings


T = TypeVar("T", bound="CreateSegment")


@_attrs_define
class CreateSegment:
    """Create a Segment.

    Attributes:
        title (str): The title of the Segment.
        description (str | Unset): The description of the Segment.
        priority (int | Unset): The priority of the Segment.
        track_unallocated (bool | Unset): Track Unallocated Costs which are not assigned to any of the created Segments.
            Default: False.
        report_settings (CreateSegmentReportSettings | Unset): Report settings configurable on top-level Segments.
        workspace_token (str | Unset): The token of the Workspace to add the Segment to. Ignored if 'segment_token' is
            set. Required if the API token is associated with multiple Workspaces.
        filter_ (str | Unset): The filter query language to apply to the Segment. Additional documentation available at
            https://docs.vantage.sh/vql.
        parent_segment_token (str | Unset): The token of the parent Segment this new Segment belongs to. Determines the
            Workspace the segment is assigned to.
    """

    title: str
    description: str | Unset = UNSET
    priority: int | Unset = UNSET
    track_unallocated: bool | Unset = False
    report_settings: CreateSegmentReportSettings | Unset = UNSET
    workspace_token: str | Unset = UNSET
    filter_: str | Unset = UNSET
    parent_segment_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        priority = self.priority

        track_unallocated = self.track_unallocated

        report_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report_settings, Unset):
            report_settings = self.report_settings.to_dict()

        workspace_token = self.workspace_token

        filter_ = self.filter_

        parent_segment_token = self.parent_segment_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if track_unallocated is not UNSET:
            field_dict["track_unallocated"] = track_unallocated
        if report_settings is not UNSET:
            field_dict["report_settings"] = report_settings
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if parent_segment_token is not UNSET:
            field_dict["parent_segment_token"] = parent_segment_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_segment_report_settings import CreateSegmentReportSettings

        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description", UNSET)

        priority = d.pop("priority", UNSET)

        track_unallocated = d.pop("track_unallocated", UNSET)

        _report_settings = d.pop("report_settings", UNSET)
        report_settings: CreateSegmentReportSettings | Unset
        if isinstance(_report_settings, Unset):
            report_settings = UNSET
        else:
            report_settings = CreateSegmentReportSettings.from_dict(_report_settings)

        workspace_token = d.pop("workspace_token", UNSET)

        filter_ = d.pop("filter", UNSET)

        parent_segment_token = d.pop("parent_segment_token", UNSET)

        create_segment = cls(
            title=title,
            description=description,
            priority=priority,
            track_unallocated=track_unallocated,
            report_settings=report_settings,
            workspace_token=workspace_token,
            filter_=filter_,
            parent_segment_token=parent_segment_token,
        )

        create_segment.additional_properties = d
        return create_segment

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
