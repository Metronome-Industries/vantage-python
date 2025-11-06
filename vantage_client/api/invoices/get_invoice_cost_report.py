from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_report import CostReport
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    invoice_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/invoices/{invoice_token}/cost_report",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostReport | Errors | None:
    if response.status_code == 200:
        response_200 = CostReport.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostReport | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[CostReport | Errors]:
    """Get cost report URL

     Get cost report URL for invoice period.

    Args:
        invoice_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostReport | Errors]
    """

    kwargs = _get_kwargs(
        invoice_token=invoice_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
) -> CostReport | Errors | None:
    """Get cost report URL

     Get cost report URL for invoice period.

    Args:
        invoice_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostReport | Errors
    """

    return sync_detailed(
        invoice_token=invoice_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[CostReport | Errors]:
    """Get cost report URL

     Get cost report URL for invoice period.

    Args:
        invoice_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostReport | Errors]
    """

    kwargs = _get_kwargs(
        invoice_token=invoice_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
) -> CostReport | Errors | None:
    """Get cost report URL

     Get cost report URL for invoice period.

    Args:
        invoice_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostReport | Errors
    """

    return (
        await asyncio_detailed(
            invoice_token=invoice_token,
            client=client,
        )
    ).parsed
