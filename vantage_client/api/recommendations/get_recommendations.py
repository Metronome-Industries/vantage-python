from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_recommendations_category import GetRecommendationsCategory
from ...models.recommendations import Recommendations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_token: str | Unset = UNSET,
    provider_account_id: str | Unset = UNSET,
    category: GetRecommendationsCategory | Unset = UNSET,
    provider: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspace_token"] = workspace_token

    params["provider_account_id"] = provider_account_id

    json_category: str | Unset = UNSET
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Recommendations | None:
    if response.status_code == 200:
        response_200 = Recommendations.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Recommendations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
    provider_account_id: str | Unset = UNSET,
    category: GetRecommendationsCategory | Unset = UNSET,
    provider: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Recommendations]:
    """Get all recommendations

     Return all Recommendations.

    Args:
        workspace_token (str | Unset):
        provider_account_id (str | Unset):
        category (GetRecommendationsCategory | Unset):
        provider (str | Unset):
        page (int | Unset):
        limit (int | Unset):

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
    workspace_token: str | Unset = UNSET,
    provider_account_id: str | Unset = UNSET,
    category: GetRecommendationsCategory | Unset = UNSET,
    provider: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Recommendations | None:
    """Get all recommendations

     Return all Recommendations.

    Args:
        workspace_token (str | Unset):
        provider_account_id (str | Unset):
        category (GetRecommendationsCategory | Unset):
        provider (str | Unset):
        page (int | Unset):
        limit (int | Unset):

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
    workspace_token: str | Unset = UNSET,
    provider_account_id: str | Unset = UNSET,
    category: GetRecommendationsCategory | Unset = UNSET,
    provider: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Recommendations]:
    """Get all recommendations

     Return all Recommendations.

    Args:
        workspace_token (str | Unset):
        provider_account_id (str | Unset):
        category (GetRecommendationsCategory | Unset):
        provider (str | Unset):
        page (int | Unset):
        limit (int | Unset):

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
    workspace_token: str | Unset = UNSET,
    provider_account_id: str | Unset = UNSET,
    category: GetRecommendationsCategory | Unset = UNSET,
    provider: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Recommendations | None:
    """Get all recommendations

     Return all Recommendations.

    Args:
        workspace_token (str | Unset):
        provider_account_id (str | Unset):
        category (GetRecommendationsCategory | Unset):
        provider (str | Unset):
        page (int | Unset):
        limit (int | Unset):

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
