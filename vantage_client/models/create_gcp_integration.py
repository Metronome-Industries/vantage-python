from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateGCPIntegration")


@_attrs_define
class CreateGCPIntegration:
    """Create a GCP Integration

    Attributes:
        billing_account_id (str): GCP billing account ID.
        project_id (str): GCP project ID.
        dataset_name (str): BigQuery dataset name.
    """

    billing_account_id: str
    project_id: str
    dataset_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_account_id = self.billing_account_id

        project_id = self.project_id

        dataset_name = self.dataset_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing_account_id": billing_account_id,
                "project_id": project_id,
                "dataset_name": dataset_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_account_id = d.pop("billing_account_id")

        project_id = d.pop("project_id")

        dataset_name = d.pop("dataset_name")

        create_gcp_integration = cls(
            billing_account_id=billing_account_id,
            project_id=project_id,
            dataset_name=dataset_name,
        )

        create_gcp_integration.additional_properties = d
        return create_gcp_integration

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
