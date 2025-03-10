from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCostsUpload")


@_attrs_define
class UserCostsUpload:
    """UserCostsUpload model

    Attributes:
        token (Union[Unset, str]): The token of the UserCostsUpload. Example: usr_csts_upld_1234.
        filename (Union[Unset, str]): The filename of the uploaded costs UserCostsUpload. Example:
            usr_csts_upld_1234.parquet.
        amount (Union[Unset, str]): The total amount of the costs in the UserCostsUpload. Example: 1234.56.
        start_date (Union[Unset, str]): The start date of the costs in the UserCostsUpload. Example: 2021-01-01.
        end_date (Union[Unset, str]): The end date of the costs in the UserCostsUpload. Example: 2021-01-31.
        import_status (Union[Unset, str]): Import status of the UserCostsUpload. Example: processing.
        created_by_token (Union[Unset, str]): The token of the Creator of the UserCostsUpload. Example: usr_1234.
        created_at (Union[Unset, str]): When the UserCostsUpload was uploaded. Example: 2021-01-01 00:00:00+00:00.
    """

    token: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    import_status: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        filename = self.filename

        amount = self.amount

        start_date = self.start_date

        end_date = self.end_date

        import_status = self.import_status

        created_by_token = self.created_by_token

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if filename is not UNSET:
            field_dict["filename"] = filename
        if amount is not UNSET:
            field_dict["amount"] = amount
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if import_status is not UNSET:
            field_dict["import_status"] = import_status
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        filename = d.pop("filename", UNSET)

        amount = d.pop("amount", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        import_status = d.pop("import_status", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        user_costs_upload = cls(
            token=token,
            filename=filename,
            amount=amount,
            start_date=start_date,
            end_date=end_date,
            import_status=import_status,
            created_by_token=created_by_token,
            created_at=created_at,
        )

        user_costs_upload.additional_properties = d
        return user_costs_upload

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
