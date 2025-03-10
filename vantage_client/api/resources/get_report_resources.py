from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.resources import Resources
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource_report_token: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    include_cost: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["resource_report_token"] = resource_report_token

    params["filter"] = filter_

    params["workspace_token"] = workspace_token

    params["include_cost"] = include_cost

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/resources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, Resources]]:
    if response.status_code == 200:
        response_200 = Resources.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 402:
        response_402 = Errors.from_dict(response.json())

        return response_402
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, Resources]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resource_report_token: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    include_cost: Union[Unset, bool] = UNSET,
) -> Response[Union[Errors, Resources]]:
    """Return Resources contained in a ResourceReport

    Args:
        resource_report_token (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        workspace_token (Union[Unset, str]):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Resources]]
    """

    kwargs = _get_kwargs(
        resource_report_token=resource_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        include_cost=include_cost,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    resource_report_token: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    include_cost: Union[Unset, bool] = UNSET,
) -> Optional[Union[Errors, Resources]]:
    """Return Resources contained in a ResourceReport

    Args:
        resource_report_token (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        workspace_token (Union[Unset, str]):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Resources]
    """

    return sync_detailed(
        client=client,
        resource_report_token=resource_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        include_cost=include_cost,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource_report_token: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    include_cost: Union[Unset, bool] = UNSET,
) -> Response[Union[Errors, Resources]]:
    """Return Resources contained in a ResourceReport

    Args:
        resource_report_token (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        workspace_token (Union[Unset, str]):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Resources]]
    """

    kwargs = _get_kwargs(
        resource_report_token=resource_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        include_cost=include_cost,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resource_report_token: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    include_cost: Union[Unset, bool] = UNSET,
) -> Optional[Union[Errors, Resources]]:
    """Return Resources contained in a ResourceReport

    Args:
        resource_report_token (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        workspace_token (Union[Unset, str]):
        include_cost (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Resources]
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_report_token=resource_report_token,
            filter_=filter_,
            workspace_token=workspace_token,
            include_cost=include_cost,
        )
    ).parsed
