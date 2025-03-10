from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.get_tag_values_providers_item import GetTagValuesProvidersItem
from ...models.get_tag_values_sort_direction import GetTagValuesSortDirection
from ...models.tag_values import TagValues
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    providers: Union[Unset, list[GetTagValuesProvidersItem]] = UNSET,
    sort_direction: Union[Unset, GetTagValuesSortDirection] = GetTagValuesSortDirection.ASC,
    search_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_providers: Union[Unset, list[str]] = UNSET
    if not isinstance(providers, Unset):
        json_providers = []
        for providers_item_data in providers:
            providers_item = providers_item_data.value
            json_providers.append(providers_item)

    params["providers"] = json_providers

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["search_query"] = search_query

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tags/{key}/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, TagValues]]:
    if response.status_code == 200:
        response_200 = TagValues.from_dict(response.json())

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
) -> Response[Union[Errors, TagValues]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    providers: Union[Unset, list[GetTagValuesProvidersItem]] = UNSET,
    sort_direction: Union[Unset, GetTagValuesSortDirection] = GetTagValuesSortDirection.ASC,
    search_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Response[Union[Errors, TagValues]]:
    """Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (Union[Unset, list[GetTagValuesProvidersItem]]):
        sort_direction (Union[Unset, GetTagValuesSortDirection]):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TagValues]]
    """

    kwargs = _get_kwargs(
        key=key,
        providers=providers,
        sort_direction=sort_direction,
        search_query=search_query,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: AuthenticatedClient,
    providers: Union[Unset, list[GetTagValuesProvidersItem]] = UNSET,
    sort_direction: Union[Unset, GetTagValuesSortDirection] = GetTagValuesSortDirection.ASC,
    search_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[Errors, TagValues]]:
    """Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (Union[Unset, list[GetTagValuesProvidersItem]]):
        sort_direction (Union[Unset, GetTagValuesSortDirection]):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TagValues]
    """

    return sync_detailed(
        key=key,
        client=client,
        providers=providers,
        sort_direction=sort_direction,
        search_query=search_query,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    providers: Union[Unset, list[GetTagValuesProvidersItem]] = UNSET,
    sort_direction: Union[Unset, GetTagValuesSortDirection] = GetTagValuesSortDirection.ASC,
    search_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Response[Union[Errors, TagValues]]:
    """Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (Union[Unset, list[GetTagValuesProvidersItem]]):
        sort_direction (Union[Unset, GetTagValuesSortDirection]):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TagValues]]
    """

    kwargs = _get_kwargs(
        key=key,
        providers=providers,
        sort_direction=sort_direction,
        search_query=search_query,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
    providers: Union[Unset, list[GetTagValuesProvidersItem]] = UNSET,
    sort_direction: Union[Unset, GetTagValuesSortDirection] = GetTagValuesSortDirection.ASC,
    search_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[Errors, TagValues]]:
    """Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (Union[Unset, list[GetTagValuesProvidersItem]]):
        sort_direction (Union[Unset, GetTagValuesSortDirection]):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TagValues]
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            providers=providers,
            sort_direction=sort_direction,
            search_query=search_query,
            page=page,
            limit=limit,
        )
    ).parsed
