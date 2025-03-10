from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource import Resource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_token: str,
    *,
    include_cost: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_cost"] = include_cost

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/resources/{resource_token}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Resource]:
    if response.status_code == 200:
        response_200 = Resource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Resource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_token: str,
    *,
    client: AuthenticatedClient,
    include_cost: Union[Unset, bool] = UNSET,
) -> Response[Resource]:
    """Return a single Resource

    Args:
        resource_token (str):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Resource]
    """

    kwargs = _get_kwargs(
        resource_token=resource_token,
        include_cost=include_cost,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_token: str,
    *,
    client: AuthenticatedClient,
    include_cost: Union[Unset, bool] = UNSET,
) -> Optional[Resource]:
    """Return a single Resource

    Args:
        resource_token (str):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Resource
    """

    return sync_detailed(
        resource_token=resource_token,
        client=client,
        include_cost=include_cost,
    ).parsed


async def asyncio_detailed(
    resource_token: str,
    *,
    client: AuthenticatedClient,
    include_cost: Union[Unset, bool] = UNSET,
) -> Response[Resource]:
    """Return a single Resource

    Args:
        resource_token (str):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Resource]
    """

    kwargs = _get_kwargs(
        resource_token=resource_token,
        include_cost=include_cost,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_token: str,
    *,
    client: AuthenticatedClient,
    include_cost: Union[Unset, bool] = UNSET,
) -> Optional[Resource]:
    """Return a single Resource

    Args:
        resource_token (str):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Resource
    """

    return (
        await asyncio_detailed(
            resource_token=resource_token,
            client=client,
            include_cost=include_cost,
        )
    ).parsed
