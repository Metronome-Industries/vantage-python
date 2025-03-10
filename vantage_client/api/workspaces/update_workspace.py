from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.update_workspace_files_body import UpdateWorkspaceFilesBody
from ...models.update_workspace_json_body import UpdateWorkspaceJsonBody
from ...models.workspace import Workspace
from ...types import Response


def _get_kwargs(
    workspace_token: str,
    *,
    body: Union[
        UpdateWorkspaceJsonBody,
        UpdateWorkspaceFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/workspaces/{workspace_token}",
    }

    if isinstance(body, UpdateWorkspaceJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateWorkspaceFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, Workspace]]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, Workspace]]:
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
    body: Union[
        UpdateWorkspaceJsonBody,
        UpdateWorkspaceFilesBody,
    ],
) -> Response[Union[Errors, Workspace]]:
    """Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceJsonBody):
        body (UpdateWorkspaceFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Workspace]]
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
    body: Union[
        UpdateWorkspaceJsonBody,
        UpdateWorkspaceFilesBody,
    ],
) -> Optional[Union[Errors, Workspace]]:
    """Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceJsonBody):
        body (UpdateWorkspaceFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Workspace]
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
    body: Union[
        UpdateWorkspaceJsonBody,
        UpdateWorkspaceFilesBody,
    ],
) -> Response[Union[Errors, Workspace]]:
    """Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceJsonBody):
        body (UpdateWorkspaceFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Workspace]]
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
    body: Union[
        UpdateWorkspaceJsonBody,
        UpdateWorkspaceFilesBody,
    ],
) -> Optional[Union[Errors, Workspace]]:
    """Update a workspace

    Args:
        workspace_token (str):
        body (UpdateWorkspaceJsonBody):
        body (UpdateWorkspaceFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Workspace]
    """

    return (
        await asyncio_detailed(
            workspace_token=workspace_token,
            client=client,
            body=body,
        )
    ).parsed
