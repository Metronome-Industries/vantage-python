from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_export import DataExport
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    data_export_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data_exports/{data_export_token}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DataExport | Errors | None:
    if response.status_code == 200:
        response_200 = DataExport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 402:
        response_402 = Errors.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DataExport | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_export_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[DataExport | Errors]:
    """Get status of data export

     Get the status of a data export.

    Args:
        data_export_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataExport | Errors]
    """

    kwargs = _get_kwargs(
        data_export_token=data_export_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_export_token: str,
    *,
    client: AuthenticatedClient,
) -> DataExport | Errors | None:
    """Get status of data export

     Get the status of a data export.

    Args:
        data_export_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataExport | Errors
    """

    return sync_detailed(
        data_export_token=data_export_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_export_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[DataExport | Errors]:
    """Get status of data export

     Get the status of a data export.

    Args:
        data_export_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataExport | Errors]
    """

    kwargs = _get_kwargs(
        data_export_token=data_export_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_export_token: str,
    *,
    client: AuthenticatedClient,
) -> DataExport | Errors | None:
    """Get status of data export

     Get the status of a data export.

    Args:
        data_export_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataExport | Errors
    """

    return (
        await asyncio_detailed(
            data_export_token=data_export_token,
            client=client,
        )
    ).parsed
