from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.user import User
from ...types import Response


def _get_kwargs(
    user_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/{user_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, User]]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

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
) -> Response[Union[Errors, User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, User]]:
    """Return a specific User.

    Args:
        user_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, User]]
    """

    kwargs = _get_kwargs(
        user_token=user_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, User]]:
    """Return a specific User.

    Args:
        user_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, User]
    """

    return sync_detailed(
        user_token=user_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, User]]:
    """Return a specific User.

    Args:
        user_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, User]]
    """

    kwargs = _get_kwargs(
        user_token=user_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, User]]:
    """Return a specific User.

    Args:
        user_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, User]
    """

    return (
        await asyncio_detailed(
            user_token=user_token,
            client=client,
        )
    ).parsed
