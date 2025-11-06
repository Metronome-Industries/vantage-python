from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.update_workspace_body import UpdateWorkspaceBody
from ...models.workspace import Workspace
from ...types import Response


def _get_kwargs(
    workspace_token: str,
    *,
    body: UpdateWorkspaceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/workspaces/{workspace_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Errors | Workspace | None:
    if response.status_code == 201:
        response_201 = Workspace.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Errors | Workspace]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceBody,
) -> Response[Errors | Workspace]:
    """Update workspace

     Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Workspace]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceBody,
) -> Errors | Workspace | None:
    """Update workspace

     Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Workspace
    """

    return sync_detailed(
        workspace_token=workspace_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceBody,
) -> Response[Errors | Workspace]:
    """Update workspace

     Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Workspace]
    """

    kwargs = _get_kwargs(
        workspace_token=workspace_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceBody,
) -> Errors | Workspace | None:
    """Update workspace

     Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Workspace
    """

    return (
        await asyncio_detailed(
            workspace_token=workspace_token,
            client=client,
            body=body,
        )
    ).parsed
