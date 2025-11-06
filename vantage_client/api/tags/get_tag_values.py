from http import HTTPStatus
from typing import Any

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
    providers: list[GetTagValuesProvidersItem] | Unset = UNSET,
    sort_direction: GetTagValuesSortDirection | Unset = GetTagValuesSortDirection.ASC,
    search_query: str | Unset = UNSET,
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

    json_sort_direction: str | Unset = UNSET
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Errors | TagValues | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Errors | TagValues]:
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
    providers: list[GetTagValuesProvidersItem] | Unset = UNSET,
    sort_direction: GetTagValuesSortDirection | Unset = GetTagValuesSortDirection.ASC,
    search_query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[Errors | TagValues]:
    """Get tag values

     Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (list[GetTagValuesProvidersItem] | Unset):
        sort_direction (GetTagValuesSortDirection | Unset):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | TagValues]
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
    providers: list[GetTagValuesProvidersItem] | Unset = UNSET,
    sort_direction: GetTagValuesSortDirection | Unset = GetTagValuesSortDirection.ASC,
    search_query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Errors | TagValues | None:
    """Get tag values

     Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (list[GetTagValuesProvidersItem] | Unset):
        sort_direction (GetTagValuesSortDirection | Unset):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | TagValues
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
    providers: list[GetTagValuesProvidersItem] | Unset = UNSET,
    sort_direction: GetTagValuesSortDirection | Unset = GetTagValuesSortDirection.ASC,
    search_query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[Errors | TagValues]:
    """Get tag values

     Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (list[GetTagValuesProvidersItem] | Unset):
        sort_direction (GetTagValuesSortDirection | Unset):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | TagValues]
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
    providers: list[GetTagValuesProvidersItem] | Unset = UNSET,
    sort_direction: GetTagValuesSortDirection | Unset = GetTagValuesSortDirection.ASC,
    search_query: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 100,
) -> Errors | TagValues | None:
    """Get tag values

     Returns corresponding TagValues for a given Tag.

    Args:
        key (str):
        providers (list[GetTagValuesProvidersItem] | Unset):
        sort_direction (GetTagValuesSortDirection | Unset):  Default:
            GetTagValuesSortDirection.ASC.
        search_query (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | TagValues
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
