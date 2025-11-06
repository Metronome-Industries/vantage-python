from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget import Budget
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    budget_token: str,
    *,
    include_performance: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_performance"] = include_performance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/budgets/{budget_token}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Budget | Errors | None:
    if response.status_code == 200:
        response_200 = Budget.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Budget | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    include_performance: bool | Unset = UNSET,
) -> Response[Budget | Errors]:
    """Get budget by token

     Return a Budget.

    Args:
        budget_token (str):
        include_performance (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Budget | Errors]
    """

    kwargs = _get_kwargs(
        budget_token=budget_token,
        include_performance=include_performance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    include_performance: bool | Unset = UNSET,
) -> Budget | Errors | None:
    """Get budget by token

     Return a Budget.

    Args:
        budget_token (str):
        include_performance (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Budget | Errors
    """

    return sync_detailed(
        budget_token=budget_token,
        client=client,
        include_performance=include_performance,
    ).parsed


async def asyncio_detailed(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    include_performance: bool | Unset = UNSET,
) -> Response[Budget | Errors]:
    """Get budget by token

     Return a Budget.

    Args:
        budget_token (str):
        include_performance (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Budget | Errors]
    """

    kwargs = _get_kwargs(
        budget_token=budget_token,
        include_performance=include_performance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    include_performance: bool | Unset = UNSET,
) -> Budget | Errors | None:
    """Get budget by token

     Return a Budget.

    Args:
        budget_token (str):
        include_performance (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Budget | Errors
    """

    return (
        await asyncio_detailed(
            budget_token=budget_token,
            client=client,
            include_performance=include_performance,
        )
    ).parsed
