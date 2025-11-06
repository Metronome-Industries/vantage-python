from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.resources import Resources
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Errors | Resources | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Errors | Resources]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resource_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
) -> Response[Errors | Resources]:
    """Get resources

     Return Resources contained in a ResourceReport

    Args:
        resource_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        include_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Resources]
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
    resource_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
) -> Errors | Resources | None:
    """Get resources

     Return Resources contained in a ResourceReport

    Args:
        resource_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        include_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Resources
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
    resource_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
) -> Response[Errors | Resources]:
    """Get resources

     Return Resources contained in a ResourceReport

    Args:
        resource_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        include_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Resources]
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
    resource_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
) -> Errors | Resources | None:
    """Get resources

     Return Resources contained in a ResourceReport

    Args:
        resource_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        include_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Resources
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
