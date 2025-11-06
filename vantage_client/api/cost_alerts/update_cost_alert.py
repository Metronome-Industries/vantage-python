from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_alert import CostAlert
from ...models.errors import Errors
from ...models.update_cost_alert import UpdateCostAlert
from ...types import Response


def _get_kwargs(
    cost_alert_token: str,
    *,
    body: UpdateCostAlert,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/cost_alerts/{cost_alert_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostAlert | Errors | None:
    if response.status_code == 200:
        response_200 = CostAlert.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostAlert | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlert,
) -> Response[CostAlert | Errors]:
    """Update cost alert

     Update a Cost Alert

    Args:
        cost_alert_token (str):
        body (UpdateCostAlert): Update a Cost Alert

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlert | Errors]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlert,
) -> CostAlert | Errors | None:
    """Update cost alert

     Update a Cost Alert

    Args:
        cost_alert_token (str):
        body (UpdateCostAlert): Update a Cost Alert

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlert | Errors
    """

    return sync_detailed(
        cost_alert_token=cost_alert_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlert,
) -> Response[CostAlert | Errors]:
    """Update cost alert

     Update a Cost Alert

    Args:
        cost_alert_token (str):
        body (UpdateCostAlert): Update a Cost Alert

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlert | Errors]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlert,
) -> CostAlert | Errors | None:
    """Update cost alert

     Update a Cost Alert

    Args:
        cost_alert_token (str):
        body (UpdateCostAlert): Update a Cost Alert

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlert | Errors
    """

    return (
        await asyncio_detailed(
            cost_alert_token=cost_alert_token,
            client=client,
            body=body,
        )
    ).parsed
