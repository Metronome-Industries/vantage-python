from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_object_changes import AuditLogObjectChanges


T = TypeVar("T", bound="AuditLog")


@_attrs_define
class AuditLog:
    """AuditLog model

    Attributes:
        token (Union[Unset, str]): The unique token identifying the audit log. Example: adt_lg_1234567890abcdef.
        object_token (Union[Unset, str]): The token of the audited object. Example: rpt_1234567890abcdef.
        object_type (Union[Unset, str]): The type of the audited object. Example: Report.
        object_title (Union[Unset, str]): The title of the audited object. Example: Production Cost Report.
        event (Union[Unset, str]): The event type of the audit log. Example: record_created.
        source (Union[Unset, str]): The source of the action (console, api, developer). Example: console.
        user (Union[Unset, str]): The name of the user who performed the action.
        workspace_title (Union[Unset, str]): The name of the workspace associated with the audit log.
        workspace_token (Union[Unset, str]): The token of the workspace associated with the audit log. Example:
            wrkspc_1234567890abcdef.
        created_at (Union[Unset, str]): The date and time, in UTC, the audit log was created. ISO 8601 Formatted.
            Example: 2021-07-09T00:00:00Z.
        object_changes (Union[Unset, AuditLogObjectChanges]): The changes made to the object.
    """

    token: Union[Unset, str] = UNSET
    object_token: Union[Unset, str] = UNSET
    object_type: Union[Unset, str] = UNSET
    object_title: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    workspace_title: Union[Unset, str] = UNSET
    workspace_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    object_changes: Union[Unset, "AuditLogObjectChanges"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        object_token = self.object_token

        object_type = self.object_type

        object_title = self.object_title

        event = self.event

        source = self.source

        user = self.user

        workspace_title = self.workspace_title

        workspace_token = self.workspace_token

        created_at = self.created_at

        object_changes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_changes, Unset):
            object_changes = self.object_changes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if object_token is not UNSET:
            field_dict["object_token"] = object_token
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_title is not UNSET:
            field_dict["object_title"] = object_title
        if event is not UNSET:
            field_dict["event"] = event
        if source is not UNSET:
            field_dict["source"] = source
        if user is not UNSET:
            field_dict["user"] = user
        if workspace_title is not UNSET:
            field_dict["workspace_title"] = workspace_title
        if workspace_token is not UNSET:
            field_dict["workspace_token"] = workspace_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if object_changes is not UNSET:
            field_dict["object_changes"] = object_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_object_changes import AuditLogObjectChanges

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        object_token = d.pop("object_token", UNSET)

        object_type = d.pop("object_type", UNSET)

        object_title = d.pop("object_title", UNSET)

        event = d.pop("event", UNSET)

        source = d.pop("source", UNSET)

        user = d.pop("user", UNSET)

        workspace_title = d.pop("workspace_title", UNSET)

        workspace_token = d.pop("workspace_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        _object_changes = d.pop("object_changes", UNSET)
        object_changes: Union[Unset, AuditLogObjectChanges]
        if isinstance(_object_changes, Unset):
            object_changes = UNSET
        else:
            object_changes = AuditLogObjectChanges.from_dict(_object_changes)

        audit_log = cls(
            token=token,
            object_token=object_token,
            object_type=object_type,
            object_title=object_title,
            event=event,
            source=source,
            user=user,
            workspace_title=workspace_title,
            workspace_token=workspace_token,
            created_at=created_at,
            object_changes=object_changes,
        )

        audit_log.additional_properties = d
        return audit_log

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
