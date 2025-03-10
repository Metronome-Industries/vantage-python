from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.report_notification import ReportNotification
from ...models.update_report_notification import UpdateReportNotification
from ...types import Response


def _get_kwargs(
    report_notification_token: str,
    *,
    body: UpdateReportNotification,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/report_notifications/{report_notification_token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, ReportNotification]]:
    if response.status_code == 200:
        response_200 = ReportNotification.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
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
    body: UpdateReportNotification,
) -> Response[Union[Errors, ReportNotification]]:
    """Update a ReportNotification.

    Args:
        report_notification_token (str):
        body (UpdateReportNotification): Update a ReportNotification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ReportNotification]]
    """

    kwargs = _get_kwargs(
        report_notification_token=report_notification_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateReportNotification,
) -> Optional[Union[Errors, ReportNotification]]:
    """Update a ReportNotification.

    Args:
        report_notification_token (str):
        body (UpdateReportNotification): Update a ReportNotification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, ReportNotification]
    """

    return sync_detailed(
        report_notification_token=report_notification_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateReportNotification,
) -> Response[Union[Errors, ReportNotification]]:
    """Update a ReportNotification.

    Args:
        report_notification_token (str):
        body (UpdateReportNotification): Update a ReportNotification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, ReportNotification]]
    """

    kwargs = _get_kwargs(
        report_notification_token=report_notification_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    report_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateReportNotification,
) -> Optional[Union[Errors, ReportNotification]]:
    """Update a ReportNotification.

    Args:
        report_notification_token (str):
        body (UpdateReportNotification): Update a ReportNotification.

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
            body=body,
        )
    ).parsed
