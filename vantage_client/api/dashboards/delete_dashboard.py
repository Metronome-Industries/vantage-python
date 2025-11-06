from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard import Dashboard
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    dashboard_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/dashboards/{dashboard_token}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dashboard | Errors | None:
    if response.status_code == 204:
        response_204 = Dashboard.from_dict(response.json())

        return response_204

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dashboard | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Dashboard | Errors]:
    """Delete dashboard

     Delete a Dashboard.

    Args:
        dashboard_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Errors]
    """

    kwargs = _get_kwargs(
        dashboard_token=dashboard_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
) -> Dashboard | Errors | None:
    """Delete dashboard

     Delete a Dashboard.

    Args:
        dashboard_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Errors
    """

    return sync_detailed(
        dashboard_token=dashboard_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Dashboard | Errors]:
    """Delete dashboard

     Delete a Dashboard.

    Args:
        dashboard_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Errors]
    """

    kwargs = _get_kwargs(
        dashboard_token=dashboard_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
) -> Dashboard | Errors | None:
    """Delete dashboard

     Delete a Dashboard.

    Args:
        dashboard_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Errors
    """

    return (
        await asyncio_detailed(
            dashboard_token=dashboard_token,
            client=client,
        )
    ).parsed
