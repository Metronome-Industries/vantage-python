from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget import Budget
from ...models.errors import Errors
from ...models.update_budget import UpdateBudget
from ...types import Response


def _get_kwargs(
    budget_token: str,
    *,
    body: UpdateBudget,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/budgets/{budget_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Budget | Errors | None:
    if response.status_code == 200:
        response_200 = Budget.from_dict(response.json())

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
    body: UpdateBudget,
) -> Response[Budget | Errors]:
    """Update budget

     Update a Budget.

    Args:
        budget_token (str):
        body (UpdateBudget): Update a Budget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Budget | Errors]
    """

    kwargs = _get_kwargs(
        budget_token=budget_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudget,
) -> Budget | Errors | None:
    """Update budget

     Update a Budget.

    Args:
        budget_token (str):
        body (UpdateBudget): Update a Budget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Budget | Errors
    """

    return sync_detailed(
        budget_token=budget_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudget,
) -> Response[Budget | Errors]:
    """Update budget

     Update a Budget.

    Args:
        budget_token (str):
        body (UpdateBudget): Update a Budget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Budget | Errors]
    """

    kwargs = _get_kwargs(
        budget_token=budget_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudget,
) -> Budget | Errors | None:
    """Update budget

     Update a Budget.

    Args:
        budget_token (str):
        body (UpdateBudget): Update a Budget.

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
            body=body,
        )
    ).parsed
