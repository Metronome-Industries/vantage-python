from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_alert_events import CostAlertEvents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cost_alert_token: str,
    *,
    report_token: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["report_token"] = report_token

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/cost_alerts/{cost_alert_token}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostAlertEvents | None:
    if response.status_code == 200:
        response_200 = CostAlertEvents.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostAlertEvents]:
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
    report_token: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[CostAlertEvents]:
    """Get all cost alert events

     Get all CostAlertEvents

    Args:
        cost_alert_token (str):
        report_token (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlertEvents]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        report_token=report_token,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    report_token: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> CostAlertEvents | None:
    """Get all cost alert events

     Get all CostAlertEvents

    Args:
        cost_alert_token (str):
        report_token (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlertEvents
    """

    return sync_detailed(
        cost_alert_token=cost_alert_token,
        client=client,
        report_token=report_token,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    report_token: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[CostAlertEvents]:
    """Get all cost alert events

     Get all CostAlertEvents

    Args:
        cost_alert_token (str):
        report_token (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAlertEvents]
    """

    kwargs = _get_kwargs(
        cost_alert_token=cost_alert_token,
        report_token=report_token,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_alert_token: str,
    *,
    client: AuthenticatedClient,
    report_token: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> CostAlertEvents | None:
    """Get all cost alert events

     Get all CostAlertEvents

    Args:
        cost_alert_token (str):
        report_token (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAlertEvents
    """

    return (
        await asyncio_detailed(
            cost_alert_token=cost_alert_token,
            client=client,
            report_token=report_token,
            page=page,
            limit=limit,
        )
    ).parsed
