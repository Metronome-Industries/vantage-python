from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_services import CostServices
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspace_token"] = workspace_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cost_services",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostServices | None:
    if response.status_code == 200:
        response_200 = CostServices.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostServices]:
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
) -> Response[CostServices]:
    """Get cost services

     List CostServices available to query in a given Workspace.

    Args:
        workspace_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostServices]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
) -> CostServices | None:
    """Get cost services

     List CostServices available to query in a given Workspace.

    Args:
        workspace_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostServices
    """

    return sync_detailed(
        client=client,
        workspace_token=workspace_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
) -> Response[CostServices]:
    """Get cost services

     List CostServices available to query in a given Workspace.

    Args:
        workspace_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostServices]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_token: str | Unset = UNSET,
) -> CostServices | None:
    """Get cost services

     List CostServices available to query in a given Workspace.

    Args:
        workspace_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostServices
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_token=workspace_token,
        )
    ).parsed
