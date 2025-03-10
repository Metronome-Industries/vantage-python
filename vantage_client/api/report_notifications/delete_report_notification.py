from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.report_notification import ReportNotification
from ...types import Response


def _get_kwargs(
    report_notification_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/report_notifications/{report_notification_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, ReportNotification]]:
    if response.status_code == 204:
        response_204 = ReportNotification.from_dict(response.json())

        return response_204
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, ReportNotification]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, ReportNotification]]:
    """Delete a ReportNotification.

    Args:
        report_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ReportNotification]]
    """

    kwargs = _get_kwargs(
        report_notification_token=report_notification_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, ReportNotification]]:
    """Delete a ReportNotification.

    Args:
        report_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, ReportNotification]
    """

    return sync_detailed(
        report_notification_token=report_notification_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, ReportNotification]]:
    """Delete a ReportNotification.

    Args:
        report_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ReportNotification]]
    """

    kwargs = _get_kwargs(
        report_notification_token=report_notification_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, ReportNotification]]:
    """Delete a ReportNotification.

    Args:
        report_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, ReportNotification]
    """

    return (
        await asyncio_detailed(
            report_notification_token=report_notification_token,
            client=client,
        )
    ).parsed
