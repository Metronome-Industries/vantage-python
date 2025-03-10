from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard import Dashboard
from ...models.errors import Errors
from ...models.update_dashboard import UpdateDashboard
from ...types import Response


def _get_kwargs(
    dashboard_token: str,
    *,
    body: UpdateDashboard,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/dashboards/{dashboard_token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Dashboard, Errors]]:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Dashboard, Errors]]:
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
    body: UpdateDashboard,
) -> Response[Union[Dashboard, Errors]]:
    """Update a Dashboard.

    Args:
        dashboard_token (str):
        body (UpdateDashboard): Update a Dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dashboard, Errors]]
    """

    kwargs = _get_kwargs(
        dashboard_token=dashboard_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboard,
) -> Optional[Union[Dashboard, Errors]]:
    """Update a Dashboard.

    Args:
        dashboard_token (str):
        body (UpdateDashboard): Update a Dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dashboard, Errors]
    """

    return sync_detailed(
        dashboard_token=dashboard_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboard,
) -> Response[Union[Dashboard, Errors]]:
    """Update a Dashboard.

    Args:
        dashboard_token (str):
        body (UpdateDashboard): Update a Dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dashboard, Errors]]
    """

    kwargs = _get_kwargs(
        dashboard_token=dashboard_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboard,
) -> Optional[Union[Dashboard, Errors]]:
    """Update a Dashboard.

    Args:
        dashboard_token (str):
        body (UpdateDashboard): Update a Dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dashboard, Errors]
    """

    return (
        await asyncio_detailed(
            dashboard_token=dashboard_token,
            client=client,
            body=body,
        )
    ).parsed
