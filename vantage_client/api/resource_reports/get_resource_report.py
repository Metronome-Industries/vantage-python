from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.resource_report import ResourceReport
from ...types import Response


def _get_kwargs(
    resource_report_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/resource_reports/{resource_report_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | ResourceReport | None:
    if response.status_code == 200:
        response_200 = ResourceReport.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | ResourceReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ResourceReport]:
    """Get resource report by token

     Return a ResourceReport.

    Args:
        resource_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ResourceReport]
    """

    kwargs = _get_kwargs(
        resource_report_token=resource_report_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ResourceReport | None:
    """Get resource report by token

     Return a ResourceReport.

    Args:
        resource_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ResourceReport
    """

    return sync_detailed(
        resource_report_token=resource_report_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ResourceReport]:
    """Get resource report by token

     Return a ResourceReport.

    Args:
        resource_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ResourceReport]
    """

    kwargs = _get_kwargs(
        resource_report_token=resource_report_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ResourceReport | None:
    """Get resource report by token

     Return a ResourceReport.

    Args:
        resource_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ResourceReport
    """

    return (
        await asyncio_detailed(
            resource_report_token=resource_report_token,
            client=client,
        )
    ).parsed
