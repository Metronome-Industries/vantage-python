from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAnomalyAlert")


@_attrs_define
class UpdateAnomalyAlert:
    """Update an AnomalyAlert.

    Attributes:
        status (str): The status of the Anomaly Alert.
        feedback (Union[Unset, str]): Optional additional comments for why this alert is ignored.
    """

    status: str
    feedback: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        feedback = self.feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        feedback = d.pop("feedback", UNSET)

        update_anomaly_alert = cls(
            status=status,
            feedback=feedback,
        )

        update_anomaly_alert.additional_properties = d
        return update_anomaly_alert

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
