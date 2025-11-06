from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_alert_event import CostAlertEvent
from ...types import Response


def _get_kwargs(
    cost_alert_token: str,
    event_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/cost_alerts/{cost_alert_token}/events/{event_token}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostAlertEvent | None:
    if response.status_code == 200:
        response_200 = CostAlertEvent.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostAlertEvent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cost_alert_token: str,
    event_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[CostAlertEvent]:
    """Get cost alert event by token

     Get a CostAlertEvent

    Args:
        cost_alert_token (str):
        event_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlertEvent]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        event_token=event_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_alert_token: str,
    event_token: str,
    *,
    client: AuthenticatedClient,
) -> CostAlertEvent | None:
    """Get cost alert event by token

     Get a CostAlertEvent

    Args:
        cost_alert_token (str):
        event_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlertEvent
    """

    return sync_detailed(
        cost_alert_token=cost_alert_token,
        event_token=event_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    cost_alert_token: str,
    event_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[CostAlertEvent]:
    """Get cost alert event by token

     Get a CostAlertEvent

    Args:
        cost_alert_token (str):
        event_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlertEvent]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        event_token=event_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_alert_token: str,
    event_token: str,
    *,
    client: AuthenticatedClient,
) -> CostAlertEvent | None:
    """Get cost alert event by token

     Get a CostAlertEvent

    Args:
        cost_alert_token (str):
        event_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlertEvent
    """

    return (
        await asyncio_detailed(
            cost_alert_token=cost_alert_token,
            event_token=event_token,
            client=client,
        )
    ).parsed
