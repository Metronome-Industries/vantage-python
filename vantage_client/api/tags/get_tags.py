from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_providers_item import GetTagsProvidersItem
from ...models.get_tags_sort_direction import GetTagsSortDirection
from ...models.tags import Tags
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    providers: list[GetTagsProvidersItem] | Unset = UNSET,
    search_query: str | Unset = UNSET,
    sort_direction: GetTagsSortDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_providers: list[str] | Unset = UNSET
    if not isinstance(providers, Unset):
        json_providers = []
        for providers_item_data in providers:
            providers_item = providers_item_data.value
            json_providers.append(providers_item)

    params["providers"] = json_providers

    params["search_query"] = search_query

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Tags | None:
    if response.status_code == 200:
        response_200 = Tags.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Tags]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    providers: list[GetTagsProvidersItem] | Unset = UNSET,
    search_query: str | Unset = UNSET,
    sort_direction: GetTagsSortDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[Tags]:
    """Get all tags

     Return all Tags that the current API token has access to.

    Args:
        providers (list[GetTagsProvidersItem] | Unset):
        search_query (str | Unset):
        sort_direction (GetTagsSortDirection | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tags]
    """

    kwargs = _get_kwargs(
        providers=providers,
        search_query=search_query,
        sort_direction=sort_direction,
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
    providers: list[GetTagsProvidersItem] | Unset = UNSET,
    search_query: str | Unset = UNSET,
    sort_direction: GetTagsSortDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Tags | None:
    """Get all tags

     Return all Tags that the current API token has access to.

    Args:
        providers (list[GetTagsProvidersItem] | Unset):
        search_query (str | Unset):
        sort_direction (GetTagsSortDirection | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tags
    """

    return sync_detailed(
        client=client,
        providers=providers,
        search_query=search_query,
        sort_direction=sort_direction,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    providers: list[GetTagsProvidersItem] | Unset = UNSET,
    search_query: str | Unset = UNSET,
    sort_direction: GetTagsSortDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[Tags]:
    """Get all tags

     Return all Tags that the current API token has access to.

    Args:
        providers (list[GetTagsProvidersItem] | Unset):
        search_query (str | Unset):
        sort_direction (GetTagsSortDirection | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tags]
    """

    kwargs = _get_kwargs(
        providers=providers,
        search_query=search_query,
        sort_direction=sort_direction,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    providers: list[GetTagsProvidersItem] | Unset = UNSET,
    search_query: str | Unset = UNSET,
    sort_direction: GetTagsSortDirection | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Tags | None:
    """Get all tags

     Return all Tags that the current API token has access to.

    Args:
        providers (list[GetTagsProvidersItem] | Unset):
        search_query (str | Unset):
        sort_direction (GetTagsSortDirection | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tags
    """

    return (
        await asyncio_detailed(
            client=client,
            providers=providers,
            search_query=search_query,
            sort_direction=sort_direction,
            page=page,
            limit=limit,
        )
    ).parsed
