from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_integrations_provider import GetIntegrationsProvider
from ...models.integrations import Integrations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider: GetIntegrationsProvider | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_provider: str | Unset = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value

    params["provider"] = json_provider

    params["account_identifier"] = account_identifier

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/integrations",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Integrations | None:
    if response.status_code == 200:
        response_200 = Integrations.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Integrations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider: GetIntegrationsProvider | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Integrations]:
    """Get all integrations

     Return all Integrations.

    Args:
        provider (GetIntegrationsProvider | Unset):
        account_identifier (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Integrations]
    """

    kwargs = _get_kwargs(
        provider=provider,
        account_identifier=account_identifier,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider: GetIntegrationsProvider | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Integrations | None:
    """Get all integrations

     Return all Integrations.

    Args:
        provider (GetIntegrationsProvider | Unset):
        account_identifier (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Integrations
    """

    return sync_detailed(
        client=client,
        provider=provider,
        account_identifier=account_identifier,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider: GetIntegrationsProvider | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Integrations]:
    """Get all integrations

     Return all Integrations.

    Args:
        provider (GetIntegrationsProvider | Unset):
        account_identifier (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Integrations]
    """

    kwargs = _get_kwargs(
        provider=provider,
        account_identifier=account_identifier,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider: GetIntegrationsProvider | Unset = UNSET,
    account_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Integrations | None:
    """Get all integrations

     Return all Integrations.

    Args:
        provider (GetIntegrationsProvider | Unset):
        account_identifier (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Integrations
    """

    return (
        await asyncio_detailed(
            client=client,
            provider=provider,
            account_identifier=account_identifier,
            page=page,
            limit=limit,
        )
    ).parsed
