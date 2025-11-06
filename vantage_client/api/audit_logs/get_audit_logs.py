from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_logs import AuditLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user: int | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    action: str | Unset = UNSET,
    object_name: str | Unset = UNSET,
    source: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    token: str | Unset = UNSET,
    object_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["user"] = user

    params["workspace_token"] = workspace_token

    params["action"] = action

    params["object_name"] = object_name

    params["source"] = source

    params["object_type"] = object_type

    params["token"] = token

    params["object_token"] = object_token

    params["start_date"] = start_date

    params["end_date"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit_logs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuditLogs | None:
    if response.status_code == 200:
        response_200 = AuditLogs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuditLogs]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user: int | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    action: str | Unset = UNSET,
    object_name: str | Unset = UNSET,
    source: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    token: str | Unset = UNSET,
    object_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> Response[AuditLogs]:
    """Get all audit logs

     Return all AuditLogs.

    Args:
        page (int | Unset):
        limit (int | Unset):
        user (int | Unset):
        workspace_token (str | Unset):
        action (str | Unset):
        object_name (str | Unset):
        source (str | Unset):
        object_type (str | Unset):
        token (str | Unset):
        object_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogs]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        user=user,
        workspace_token=workspace_token,
        action=action,
        object_name=object_name,
        source=source,
        object_type=object_type,
        token=token,
        object_token=object_token,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user: int | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    action: str | Unset = UNSET,
    object_name: str | Unset = UNSET,
    source: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    token: str | Unset = UNSET,
    object_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> AuditLogs | None:
    """Get all audit logs

     Return all AuditLogs.

    Args:
        page (int | Unset):
        limit (int | Unset):
        user (int | Unset):
        workspace_token (str | Unset):
        action (str | Unset):
        object_name (str | Unset):
        source (str | Unset):
        object_type (str | Unset):
        token (str | Unset):
        object_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogs
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        user=user,
        workspace_token=workspace_token,
        action=action,
        object_name=object_name,
        source=source,
        object_type=object_type,
        token=token,
        object_token=object_token,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user: int | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    action: str | Unset = UNSET,
    object_name: str | Unset = UNSET,
    source: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    token: str | Unset = UNSET,
    object_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> Response[AuditLogs]:
    """Get all audit logs

     Return all AuditLogs.

    Args:
        page (int | Unset):
        limit (int | Unset):
        user (int | Unset):
        workspace_token (str | Unset):
        action (str | Unset):
        object_name (str | Unset):
        source (str | Unset):
        object_type (str | Unset):
        token (str | Unset):
        object_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogs]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        user=user,
        workspace_token=workspace_token,
        action=action,
        object_name=object_name,
        source=source,
        object_type=object_type,
        token=token,
        object_token=object_token,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    user: int | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    action: str | Unset = UNSET,
    object_name: str | Unset = UNSET,
    source: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    token: str | Unset = UNSET,
    object_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> AuditLogs | None:
    """Get all audit logs

     Return all AuditLogs.

    Args:
        page (int | Unset):
        limit (int | Unset):
        user (int | Unset):
        workspace_token (str | Unset):
        action (str | Unset):
        object_name (str | Unset):
        source (str | Unset):
        object_type (str | Unset):
        token (str | Unset):
        object_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogs
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            user=user,
            workspace_token=workspace_token,
            action=action,
            object_name=object_name,
            source=source,
            object_type=object_type,
            token=token,
            object_token=object_token,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
