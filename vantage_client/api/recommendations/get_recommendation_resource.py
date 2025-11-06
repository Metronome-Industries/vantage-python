from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.provider_resource import ProviderResource
from ...types import Response


def _get_kwargs(
    recommendation_token: str,
    resource_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/recommendations/{recommendation_token}/resources/{resource_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | ProviderResource | None:
    if response.status_code == 200:
        response_200 = ProviderResource.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | ProviderResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recommendation_token: str,
    resource_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ProviderResource]:
    """Get specific resource for a recommendation

     Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.

    Args:
        recommendation_token (str):
        resource_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ProviderResource]
    """

    kwargs = _get_kwargs(
        recommendation_token=recommendation_token,
        resource_token=resource_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    recommendation_token: str,
    resource_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ProviderResource | None:
    """Get specific resource for a recommendation

     Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.

    Args:
        recommendation_token (str):
        resource_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ProviderResource
    """

    return sync_detailed(
        recommendation_token=recommendation_token,
        resource_token=resource_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    recommendation_token: str,
    resource_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | ProviderResource]:
    """Get specific resource for a recommendation

     Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.

    Args:
        recommendation_token (str):
        resource_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | ProviderResource]
    """

    kwargs = _get_kwargs(
        recommendation_token=recommendation_token,
        resource_token=resource_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    recommendation_token: str,
    resource_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | ProviderResource | None:
    """Get specific resource for a recommendation

     Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.

    Args:
        recommendation_token (str):
        resource_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | ProviderResource
    """

    return (
        await asyncio_detailed(
            recommendation_token=recommendation_token,
            resource_token=resource_token,
            client=client,
        )
    ).parsed
