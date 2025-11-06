from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_unit_costs_export_body import CreateUnitCostsExportBody
from ...models.data_export import DataExport
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUnitCostsExportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/unit_costs/data_exports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DataExport | Errors | None:
    if response.status_code == 202:
        response_202 = DataExport.from_dict(response.json())

        return response_202

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
    *,
    client: AuthenticatedClient,
    body: CreateUnitCostsExportBody,
) -> Response[DataExport | Errors]:
    """Generate data export of unit costs

     Generate a DataExport of unit costs.

    Args:
        body (CreateUnitCostsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataExport | Errors]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateUnitCostsExportBody,
) -> DataExport | Errors | None:
    """Generate data export of unit costs

     Generate a DataExport of unit costs.

    Args:
        body (CreateUnitCostsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataExport | Errors
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUnitCostsExportBody,
) -> Response[DataExport | Errors]:
    """Generate data export of unit costs

     Generate a DataExport of unit costs.

    Args:
        body (CreateUnitCostsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataExport | Errors]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUnitCostsExportBody,
) -> DataExport | Errors | None:
    """Generate data export of unit costs

     Generate a DataExport of unit costs.

    Args:
        body (CreateUnitCostsExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataExport | Errors
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
