from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_log import AuditLog
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    audit_log_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/audit_logs/{audit_log_token}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuditLog | Errors | None:
    if response.status_code == 200:
        response_200 = AuditLog.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuditLog | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audit_log_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[AuditLog | Errors]:
    """Get audit log by token

     Return a specific AuditLog.

    Args:
        audit_log_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLog | Errors]
    """

    kwargs = _get_kwargs(
        audit_log_token=audit_log_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audit_log_token: str,
    *,
    client: AuthenticatedClient,
) -> AuditLog | Errors | None:
    """Get audit log by token

     Return a specific AuditLog.

    Args:
        audit_log_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLog | Errors
    """

    return sync_detailed(
        audit_log_token=audit_log_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    audit_log_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[AuditLog | Errors]:
    """Get audit log by token

     Return a specific AuditLog.

    Args:
        audit_log_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLog | Errors]
    """

    kwargs = _get_kwargs(
        audit_log_token=audit_log_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audit_log_token: str,
    *,
    client: AuthenticatedClient,
) -> AuditLog | Errors | None:
    """Get audit log by token

     Return a specific AuditLog.

    Args:
        audit_log_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLog | Errors
    """

    return (
        await asyncio_detailed(
            audit_log_token=audit_log_token,
            client=client,
        )
    ).parsed
