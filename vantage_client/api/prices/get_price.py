from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.price import Price
from ...types import Response


def _get_kwargs(
    product_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/products/{product_id}/prices/{id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Price]:
    if response.status_code == 200:
        response_200 = Price.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Price]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Price]:
    """Returns a price

    Args:
        product_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Price]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Price]:
    """Returns a price

    Args:
        product_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Price
    """

    return sync_detailed(
        product_id=product_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Price]:
    """Returns a price

    Args:
        product_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Price]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Price]:
    """Returns a price

    Args:
        product_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Price
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            id=id,
            client=client,
        )
    ).parsed
