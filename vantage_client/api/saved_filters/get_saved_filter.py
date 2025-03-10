from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.saved_filter import SavedFilter
from ...types import Response


def _get_kwargs(
    saved_filter_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/saved_filters/{saved_filter_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, SavedFilter]]:
    if response.status_code == 200:
        response_200 = SavedFilter.from_dict(response.json())

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
) -> Response[Union[Errors, SavedFilter]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    saved_filter_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, SavedFilter]]:
    """Return a specific SavedFilter.

    Args:
        saved_filter_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, SavedFilter]]
    """

    kwargs = _get_kwargs(
        saved_filter_token=saved_filter_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    saved_filter_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, SavedFilter]]:
    """Return a specific SavedFilter.

    Args:
        saved_filter_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, SavedFilter]
    """

    return sync_detailed(
        saved_filter_token=saved_filter_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    saved_filter_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, SavedFilter]]:
    """Return a specific SavedFilter.

    Args:
        saved_filter_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, SavedFilter]]
    """

    kwargs = _get_kwargs(
        saved_filter_token=saved_filter_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    saved_filter_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, SavedFilter]]:
    """Return a specific SavedFilter.

    Args:
        saved_filter_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, SavedFilter]
    """

    return (
        await asyncio_detailed(
            saved_filter_token=saved_filter_token,
            client=client,
        )
    ).parsed
