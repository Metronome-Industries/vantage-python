from http import HTTPStatus
from typing import Any, Optional, Union

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
        "method": "delete",
        "url": f"/managed_accounts/{managed_account_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, ManagedAccount]]:
    if response.status_code == 204:
        response_204 = ManagedAccount.from_dict(response.json())

        return response_204
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, ManagedAccount]]:
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
) -> Response[Union[Errors, ManagedAccount]]:
    """Delete a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ManagedAccount]]
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
) -> Optional[Union[Errors, ManagedAccount]]:
    """Delete a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, ManagedAccount]
    """

    return sync_detailed(
        managed_account_token=managed_account_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    managed_account_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, ManagedAccount]]:
    """Delete a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ManagedAccount]]
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
) -> Optional[Union[Errors, ManagedAccount]]:
    """Delete a Managed Account.

    Args:
        managed_account_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, ManagedAccount]
    """

    return (
        await asyncio_detailed(
            managed_account_token=managed_account_token,
            client=client,
        )
    ).parsed
