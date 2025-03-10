from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.update_virtual_tag_config import UpdateVirtualTagConfig
from ...models.virtual_tag_config import VirtualTagConfig
from ...types import Response


def _get_kwargs(
    token: str,
    *,
    body: UpdateVirtualTagConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/virtual_tag_configs/{token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, VirtualTagConfig]]:
    if response.status_code == 200:
        response_200 = VirtualTagConfig.from_dict(response.json())

        return response_200
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, VirtualTagConfig]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagConfig,
) -> Response[Union[Errors, VirtualTagConfig]]:
    """Updates an existing VirtualTagConfig.

    Args:
        token (str):
        body (UpdateVirtualTagConfig): Updates an existing VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, VirtualTagConfig]]
    """

    kwargs = _get_kwargs(
        token=token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagConfig,
) -> Optional[Union[Errors, VirtualTagConfig]]:
    """Updates an existing VirtualTagConfig.

    Args:
        token (str):
        body (UpdateVirtualTagConfig): Updates an existing VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, VirtualTagConfig]
    """

    return sync_detailed(
        token=token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagConfig,
) -> Response[Union[Errors, VirtualTagConfig]]:
    """Updates an existing VirtualTagConfig.

    Args:
        token (str):
        body (UpdateVirtualTagConfig): Updates an existing VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, VirtualTagConfig]]
    """

    kwargs = _get_kwargs(
        token=token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagConfig,
) -> Optional[Union[Errors, VirtualTagConfig]]:
    """Updates an existing VirtualTagConfig.

    Args:
        token (str):
        body (UpdateVirtualTagConfig): Updates an existing VirtualTagConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, VirtualTagConfig]
    """

    return (
        await asyncio_detailed(
            token=token,
            client=client,
            body=body,
        )
    ).parsed
