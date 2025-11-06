from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_provider_accounts import CostProviderAccounts
from ...models.get_cost_provider_accounts_provider import GetCostProviderAccountsProvider
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_token: str | Unset = UNSET,
    provider: GetCostProviderAccountsProvider | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspace_token"] = workspace_token

    json_provider: str | Unset = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value

    params["provider"] = json_provider

    params["account_id"] = account_id

    params["account_name"] = account_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cost_provider_accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostProviderAccounts | None:
    if response.status_code == 200:
        response_200 = CostProviderAccounts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CostProviderAccounts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
    provider: GetCostProviderAccountsProvider | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_name: str | Unset = UNSET,
) -> Response[CostProviderAccounts]:
    """Get all cost provider accounts

     List CostProviderAccounts available in a given Workspace.

    Args:
        workspace_token (str | Unset):
        provider (GetCostProviderAccountsProvider | Unset):
        account_id (str | Unset):
        account_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostProviderAccounts]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        provider=provider,
        account_id=account_id,
        account_name=account_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
    provider: GetCostProviderAccountsProvider | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_name: str | Unset = UNSET,
) -> CostProviderAccounts | None:
    """Get all cost provider accounts

     List CostProviderAccounts available in a given Workspace.

    Args:
        workspace_token (str | Unset):
        provider (GetCostProviderAccountsProvider | Unset):
        account_id (str | Unset):
        account_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostProviderAccounts
    """

    return sync_detailed(
        client=client,
        workspace_token=workspace_token,
        provider=provider,
        account_id=account_id,
        account_name=account_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
    provider: GetCostProviderAccountsProvider | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_name: str | Unset = UNSET,
) -> Response[CostProviderAccounts]:
    """Get all cost provider accounts

     List CostProviderAccounts available in a given Workspace.

    Args:
        workspace_token (str | Unset):
        provider (GetCostProviderAccountsProvider | Unset):
        account_id (str | Unset):
        account_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostProviderAccounts]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        provider=provider,
        account_id=account_id,
        account_name=account_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
    provider: GetCostProviderAccountsProvider | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_name: str | Unset = UNSET,
) -> CostProviderAccounts | None:
    """Get all cost provider accounts

     List CostProviderAccounts available in a given Workspace.

    Args:
        workspace_token (str | Unset):
        provider (GetCostProviderAccountsProvider | Unset):
        account_id (str | Unset):
        account_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostProviderAccounts
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_token=workspace_token,
            provider=provider,
            account_id=account_id,
            account_name=account_name,
        )
    ).parsed
