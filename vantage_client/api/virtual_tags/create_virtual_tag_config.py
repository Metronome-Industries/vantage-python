from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_virtual_tag_config import CreateVirtualTagConfig
from ...models.errors import Errors
from ...models.virtual_tag_config import VirtualTagConfig
from ...types import Response


def _get_kwargs(
    *,
    body: CreateVirtualTagConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/virtual_tag_configs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | VirtualTagConfig | None:
    if response.status_code == 201:
        response_201 = VirtualTagConfig.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | VirtualTagConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateVirtualTagConfig,
) -> Response[Errors | VirtualTagConfig]:
    """Create virtual tag config

     Create a new VirtualTagConfig.

    Args:
        body (CreateVirtualTagConfig): Create a new VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | VirtualTagConfig]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateVirtualTagConfig,
) -> Errors | VirtualTagConfig | None:
    """Create virtual tag config

     Create a new VirtualTagConfig.

    Args:
        body (CreateVirtualTagConfig): Create a new VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | VirtualTagConfig
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateVirtualTagConfig,
) -> Response[Errors | VirtualTagConfig]:
    """Create virtual tag config

     Create a new VirtualTagConfig.

    Args:
        body (CreateVirtualTagConfig): Create a new VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | VirtualTagConfig]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateVirtualTagConfig,
) -> Errors | VirtualTagConfig | None:
    """Create virtual tag config

     Create a new VirtualTagConfig.

    Args:
        body (CreateVirtualTagConfig): Create a new VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | VirtualTagConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
