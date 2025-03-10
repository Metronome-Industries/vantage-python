from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_costs_upload_via_csv_data_body import (
    CreateUserCostsUploadViaCsvDataBody,
)
from ...models.create_user_costs_upload_via_csv_files_body import (
    CreateUserCostsUploadViaCsvFilesBody,
)
from ...models.errors import Errors
from ...models.user_costs_upload import UserCostsUpload
from ...types import Response


def _get_kwargs(
    integration_token: str,
    *,
    body: Union[
        CreateUserCostsUploadViaCsvDataBody,
        CreateUserCostsUploadViaCsvFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/integrations/{integration_token}/costs.csv",
    }

    if isinstance(body, CreateUserCostsUploadViaCsvDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreateUserCostsUploadViaCsvFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, UserCostsUpload]]:
    if response.status_code == 201:
        response_201 = UserCostsUpload.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, UserCostsUpload]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUserCostsUploadViaCsvDataBody,
        CreateUserCostsUploadViaCsvFilesBody,
    ],
) -> Response[Union[Errors, UserCostsUpload]]:
    """Create UserCostsUpload via CSV for a Custom Provider Integration.

    Args:
        integration_token (str):
        body (CreateUserCostsUploadViaCsvDataBody):
        body (CreateUserCostsUploadViaCsvFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, UserCostsUpload]]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUserCostsUploadViaCsvDataBody,
        CreateUserCostsUploadViaCsvFilesBody,
    ],
) -> Optional[Union[Errors, UserCostsUpload]]:
    """Create UserCostsUpload via CSV for a Custom Provider Integration.

    Args:
        integration_token (str):
        body (CreateUserCostsUploadViaCsvDataBody):
        body (CreateUserCostsUploadViaCsvFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, UserCostsUpload]
    """

    return sync_detailed(
        integration_token=integration_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    integration_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUserCostsUploadViaCsvDataBody,
        CreateUserCostsUploadViaCsvFilesBody,
    ],
) -> Response[Union[Errors, UserCostsUpload]]:
    """Create UserCostsUpload via CSV for a Custom Provider Integration.

    Args:
        integration_token (str):
        body (CreateUserCostsUploadViaCsvDataBody):
        body (CreateUserCostsUploadViaCsvFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, UserCostsUpload]]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUserCostsUploadViaCsvDataBody,
        CreateUserCostsUploadViaCsvFilesBody,
    ],
) -> Optional[Union[Errors, UserCostsUpload]]:
    """Create UserCostsUpload via CSV for a Custom Provider Integration.

    Args:
        integration_token (str):
        body (CreateUserCostsUploadViaCsvDataBody):
        body (CreateUserCostsUploadViaCsvFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, UserCostsUpload]
    """

    return (
        await asyncio_detailed(
            integration_token=integration_token,
            client=client,
            body=body,
        )
    ).parsed
