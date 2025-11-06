from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_invoice import DownloadInvoice
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    invoice_token: str,
    *,
    body: DownloadInvoice,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/invoices/{invoice_token}/download",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Errors | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Errors]:
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
    body: DownloadInvoice,
) -> Response[Any | Errors]:
    """Get invoice file

     Download invoice file (PDF or CSV).

    Args:
        invoice_token (str):
        body (DownloadInvoice): Download invoice file (PDF or CSV).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        invoice_token=invoice_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
    body: DownloadInvoice,
) -> Any | Errors | None:
    """Get invoice file

     Download invoice file (PDF or CSV).

    Args:
        invoice_token (str):
        body (DownloadInvoice): Download invoice file (PDF or CSV).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return sync_detailed(
        invoice_token=invoice_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
    body: DownloadInvoice,
) -> Response[Any | Errors]:
    """Get invoice file

     Download invoice file (PDF or CSV).

    Args:
        invoice_token (str):
        body (DownloadInvoice): Download invoice file (PDF or CSV).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        invoice_token=invoice_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_token: str,
    *,
    client: AuthenticatedClient,
    body: DownloadInvoice,
) -> Any | Errors | None:
    """Get invoice file

     Download invoice file (PDF or CSV).

    Args:
        invoice_token (str):
        body (DownloadInvoice): Download invoice file (PDF or CSV).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return (
        await asyncio_detailed(
            invoice_token=invoice_token,
            client=client,
            body=body,
        )
    ).parsed
