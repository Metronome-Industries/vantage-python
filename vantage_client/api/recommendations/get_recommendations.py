from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_recommendations_category import GetRecommendationsCategory
from ...models.recommendations import Recommendations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_token: Union[Unset, str] = UNSET,
    provider_account_id: Union[Unset, str] = UNSET,
    category: Union[Unset, GetRecommendationsCategory] = UNSET,
    provider: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspace_token"] = workspace_token

    params["provider_account_id"] = provider_account_id

    json_category: Union[Unset, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params["provider"] = provider

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recommendations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Recommendations]:
    if response.status_code == 200:
        response_200 = Recommendations.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Recommendations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: Union[Unset, str] = UNSET,
    provider_account_id: Union[Unset, str] = UNSET,
    category: Union[Unset, GetRecommendationsCategory] = UNSET,
    provider: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Recommendations]:
    """Return all Recommendations.

    Args:
        workspace_token (Union[Unset, str]):
        provider_account_id (Union[Unset, str]):
        category (Union[Unset, GetRecommendationsCategory]):
        provider (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Recommendations]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        provider_account_id=provider_account_id,
        category=category,
        provider=provider,
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
    workspace_token: Union[Unset, str] = UNSET,
    provider_account_id: Union[Unset, str] = UNSET,
    category: Union[Unset, GetRecommendationsCategory] = UNSET,
    provider: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Recommendations]:
    """Return all Recommendations.

    Args:
        workspace_token (Union[Unset, str]):
        provider_account_id (Union[Unset, str]):
        category (Union[Unset, GetRecommendationsCategory]):
        provider (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Recommendations
    """

    return sync_detailed(
        client=client,
        workspace_token=workspace_token,
        provider_account_id=provider_account_id,
        category=category,
        provider=provider,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: Union[Unset, str] = UNSET,
    provider_account_id: Union[Unset, str] = UNSET,
    category: Union[Unset, GetRecommendationsCategory] = UNSET,
    provider: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Recommendations]:
    """Return all Recommendations.

    Args:
        workspace_token (Union[Unset, str]):
        provider_account_id (Union[Unset, str]):
        category (Union[Unset, GetRecommendationsCategory]):
        provider (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Recommendations]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        provider_account_id=provider_account_id,
        category=category,
        provider=provider,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_token: Union[Unset, str] = UNSET,
    provider_account_id: Union[Unset, str] = UNSET,
    category: Union[Unset, GetRecommendationsCategory] = UNSET,
    provider: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Recommendations]:
    """Return all Recommendations.

    Args:
        workspace_token (Union[Unset, str]):
        provider_account_id (Union[Unset, str]):
        category (Union[Unset, GetRecommendationsCategory]):
        provider (Union[Unset, str]):
        page (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Recommendations
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_token=workspace_token,
            provider_account_id=provider_account_id,
            category=category,
            provider=provider,
            page=page,
            limit=limit,
        )
    ).parsed
