from http import HTTPStatus
from typing import Any, Optional, Union

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
        "method": "get",
        "url": f"/budget_alerts/{budget_alert_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BudgetAlert, Errors]]:
    if response.status_code == 200:
        response_200 = BudgetAlert.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BudgetAlert, Errors]]:
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
) -> Response[Union[BudgetAlert, Errors]]:
    """Return a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
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
) -> Optional[Union[BudgetAlert, Errors]]:
    """Return a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return sync_detailed(
        budget_alert_token=budget_alert_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BudgetAlert, Errors]]:
    """Return a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
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
) -> Optional[Union[BudgetAlert, Errors]]:
    """Return a BudgetAlert.

    Args:
        budget_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return (
        await asyncio_detailed(
            budget_alert_token=budget_alert_token,
            client=client,
        )
    ).parsed
