from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_alert import BudgetAlert
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    budget_alert_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/budget_alerts/{budget_alert_token}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BudgetAlert | Errors | None:
    if response.status_code == 204:
        response_204 = BudgetAlert.from_dict(response.json())

        return response_204

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BudgetAlert | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BudgetAlert | Errors]:
    """Delete budget alert

     Delete a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetAlert | Errors]
    """

    kwargs = _get_kwargs(
        budget_alert_token=budget_alert_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> BudgetAlert | Errors | None:
    """Delete budget alert

     Delete a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetAlert | Errors
    """

    return sync_detailed(
        budget_alert_token=budget_alert_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BudgetAlert | Errors]:
    """Delete budget alert

     Delete a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetAlert | Errors]
    """

    kwargs = _get_kwargs(
        budget_alert_token=budget_alert_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> BudgetAlert | Errors | None:
    """Delete budget alert

     Delete a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetAlert | Errors
    """

    return (
        await asyncio_detailed(
            budget_alert_token=budget_alert_token,
            client=client,
        )
    ).parsed
