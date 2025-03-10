from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateAzureIntegration")


@_attrs_define
class CreateAzureIntegration:
    """Create an Azure Integration

    Attributes:
        tenant (str): Azure AD Tenant ID.
        app_id (str): Service Principal Application ID.
        password (str): Service Principal Password.
    """

    tenant: str
    app_id: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant = self.tenant

        app_id = self.app_id

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant": tenant,
                "app_id": app_id,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tenant = d.pop("tenant")

        app_id = d.pop("app_id")

        password = d.pop("password")

        create_azure_integration = cls(
            tenant=tenant,
            app_id=app_id,
            password=password,
        )

        create_azure_integration.additional_properties = d
        return create_azure_integration

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
