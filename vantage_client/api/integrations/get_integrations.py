from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_integrations_provider import GetIntegrationsProvider
from ...models.integrations import Integrations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider: Union[Unset, GetIntegrationsProvider] = UNSET,
    account_identifier: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_provider: Union[Unset, str] = UNSET
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Integrations]:
    if response.status_code == 200:
        response_200 = Integrations.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Integrations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, GetIntegrationsProvider] = UNSET,
    account_identifier: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Integrations]:
    """Return all Integrations.

    Args:
        provider (Union[Unset, GetIntegrationsProvider]):
        account_identifier (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

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
    provider: Union[Unset, GetIntegrationsProvider] = UNSET,
    account_identifier: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Integrations]:
    """Return all Integrations.

    Args:
        provider (Union[Unset, GetIntegrationsProvider]):
        account_identifier (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

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
    provider: Union[Unset, GetIntegrationsProvider] = UNSET,
    account_identifier: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Integrations]:
    """Return all Integrations.

    Args:
        provider (Union[Unset, GetIntegrationsProvider]):
        account_identifier (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

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
    provider: Union[Unset, GetIntegrationsProvider] = UNSET,
    account_identifier: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Integrations]:
    """Return all Integrations.

    Args:
        provider (Union[Unset, GetIntegrationsProvider]):
        account_identifier (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

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
