from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_logs import AuditLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    user: Union[Unset, int] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
    object_token: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AuditLogs]:
    if response.status_code == 200:
        response_200 = AuditLogs.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AuditLogs]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    user: Union[Unset, int] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
    object_token: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Response[AuditLogs]:
    """Return all AuditLogs.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        user (Union[Unset, int]):
        workspace_token (Union[Unset, str]):
        action (Union[Unset, str]):
        object_name (Union[Unset, str]):
        source (Union[Unset, str]):
        object_type (Union[Unset, str]):
        token (Union[Unset, str]):
        object_token (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

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
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    user: Union[Unset, int] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
    object_token: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Optional[AuditLogs]:
    """Return all AuditLogs.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        user (Union[Unset, int]):
        workspace_token (Union[Unset, str]):
        action (Union[Unset, str]):
        object_name (Union[Unset, str]):
        source (Union[Unset, str]):
        object_type (Union[Unset, str]):
        token (Union[Unset, str]):
        object_token (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

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
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    user: Union[Unset, int] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
    object_token: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Response[AuditLogs]:
    """Return all AuditLogs.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        user (Union[Unset, int]):
        workspace_token (Union[Unset, str]):
        action (Union[Unset, str]):
        object_name (Union[Unset, str]):
        source (Union[Unset, str]):
        object_type (Union[Unset, str]):
        token (Union[Unset, str]):
        object_token (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

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
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    user: Union[Unset, int] = UNSET,
    workspace_token: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
    object_token: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Optional[AuditLogs]:
    """Return all AuditLogs.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        user (Union[Unset, int]):
        workspace_token (Union[Unset, str]):
        action (Union[Unset, str]):
        object_name (Union[Unset, str]):
        source (Union[Unset, str]):
        object_type (Union[Unset, str]):
        token (Union[Unset, str]):
        object_token (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

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
