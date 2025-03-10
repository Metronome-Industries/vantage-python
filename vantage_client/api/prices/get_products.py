from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.products import Products
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider_id: Union[Unset, str] = UNSET,
    service_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["provider_id"] = provider_id

    params["service_id"] = service_id

    params["name"] = name

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/products",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Products]:
    if response.status_code == 200:
        response_200 = Products.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Products]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider_id: Union[Unset, str] = UNSET,
    service_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Products]:
    """Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2,
    Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across
    all Services and Providers but has optional query parameters for filtering listed below.

    Args:
        provider_id (Union[Unset, str]):
        service_id (Union[Unset, str]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Products]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        service_id=service_id,
        name=name,
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
    provider_id: Union[Unset, str] = UNSET,
    service_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Products]:
    """Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2,
    Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across
    all Services and Providers but has optional query parameters for filtering listed below.

    Args:
        provider_id (Union[Unset, str]):
        service_id (Union[Unset, str]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Products
    """

    return sync_detailed(
        client=client,
        provider_id=provider_id,
        service_id=service_id,
        name=name,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider_id: Union[Unset, str] = UNSET,
    service_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Products]:
    """Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2,
    Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across
    all Services and Providers but has optional query parameters for filtering listed below.

    Args:
        provider_id (Union[Unset, str]):
        service_id (Union[Unset, str]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Products]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        service_id=service_id,
        name=name,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider_id: Union[Unset, str] = UNSET,
    service_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Products]:
    """Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2,
    Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across
    all Services and Providers but has optional query parameters for filtering listed below.

    Args:
        provider_id (Union[Unset, str]):
        service_id (Union[Unset, str]):
        name (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Products
    """

    return (
        await asyncio_detailed(
            client=client,
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
    ).parsed
