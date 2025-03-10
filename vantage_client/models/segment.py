from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_report_settings import SegmentReportSettings


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """Segment model

    Attributes:
        token (Union[Unset, str]):
        title (Union[Unset, str]): The title of the Segment. Example: OPEX.
        parent_segment_token (Union[Unset, str]): The token of the parent Segment of this Segment.
        description (Union[Unset, str]): The description of the Segment. Example: Operating expenses.
        track_unallocated (Union[Unset, bool]): Track Unallocated Costs which are not assigned to any of the created
            Segments.
        report_settings (Union[Unset, SegmentReportSettings]): Report settings configurable on top-level Segments.
        priority (Union[Unset, int]): Costs are assigned in priority order across all Segments with assigned filters.
            Example: 100.
        filter_ (Union[Unset, str]): The filter applied to the Segment. Additional documentation available at
            https://docs.vantage.sh/vql.
        created_at (Union[Unset, str]): The date and time, in UTC, the Segment was created. ISO 8601 Formatted. Example:
            2021-07-09 00:00:00+00:00.
        workspace_token (Union[Unset, str]): The token for the Workspace the Segment is a part of.
        report_token (Union[Unset, str]): The token for the Report the Segment has generated.
    """

    token: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    parent_segment_token: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    track_unallocated: Union[Unset, bool] = UNSET
    report_settings: Union[Unset, "SegmentReportSettings"] = UNSET
    priority: Union[Unset, int] = UNSET
    filter_: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    report_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        parent_segment_token = self.parent_segment_token

        description = self.description

        track_unallocated = self.track_unallocated

        report_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.report_settings, Unset):
            report_settings = self.report_settings.to_dict()

        priority = self.priority

        filter_ = self.filter_

        created_at = self.created_at

        workspace_token = self.workspace_token

        report_token = self.report_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if parent_segment_token is not UNSET:
            field_dict["parent_segment_token"] = parent_segment_token
        if description is not UNSET:
            field_dict["description"] = description
        if track_unallocated is not UNSET:
            field_dict["track_unallocated"] = track_unallocated
        if report_settings is not UNSET:
            field_dict["report_settings"] = report_settings
        if priority is not UNSET:
            field_dict["priority"] = priority
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if report_token is not UNSET:
            field_dict["report_token"] = report_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.segment_report_settings import SegmentReportSettings

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        parent_segment_token = d.pop("parent_segment_token", UNSET)

        description = d.pop("description", UNSET)

        track_unallocated = d.pop("track_unallocated", UNSET)

        _report_settings = d.pop("report_settings", UNSET)
        report_settings: Union[Unset, SegmentReportSettings]
        if isinstance(_report_settings, Unset):
            report_settings = UNSET
        else:
            report_settings = SegmentReportSettings.from_dict(_report_settings)

        priority = d.pop("priority", UNSET)

        filter_ = d.pop("filter", UNSET)

        created_at = d.pop("created_at", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        report_token = d.pop("report_token", UNSET)

        segment = cls(
            token=token,
            title=title,
            parent_segment_token=parent_segment_token,
            description=description,
            track_unallocated=track_unallocated,
            report_settings=report_settings,
            priority=priority,
            filter_=filter_,
            created_at=created_at,
            workspace_token=workspace_token,
            report_token=report_token,
        )

        segment.additional_properties = d
        return segment

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
