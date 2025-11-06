from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.managed_account import ManagedAccount
from ...types import Response


def _get_kwargs(
    managed_account_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/managed_accounts/{managed_account_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | ManagedAccount | None:
    if response.status_code == 200:
        response_200 = ManagedAccount.from_dict(response.json())

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
) -> Response[Errors | ManagedAccount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    managed_account_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ManagedAccount]:
    """Get managed account by token

     Return a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ManagedAccount]
    """

    kwargs = _get_kwargs(
        managed_account_token=managed_account_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    managed_account_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ManagedAccount | None:
    """Get managed account by token

     Return a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ManagedAccount
    """

    return sync_detailed(
        managed_account_token=managed_account_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    managed_account_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ManagedAccount]:
    """Get managed account by token

     Return a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ManagedAccount]
    """

    kwargs = _get_kwargs(
        managed_account_token=managed_account_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    managed_account_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ManagedAccount | None:
    """Get managed account by token

     Return a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ManagedAccount
    """

    return (
        await asyncio_detailed(
            managed_account_token=managed_account_token,
            client=client,
        )
    ).parsed
