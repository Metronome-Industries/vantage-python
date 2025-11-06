from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_notification import AnomalyNotification
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    anomaly_notification_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/anomaly_notifications/{anomaly_notification_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnomalyNotification | Errors | None:
    if response.status_code == 200:
        response_200 = AnomalyNotification.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnomalyNotification | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[AnomalyNotification | Errors]:
    """Get anomaly notification by token

     Return an Anomaly Notification that the current API token has access to.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyNotification | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_notification_token=anomaly_notification_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> AnomalyNotification | Errors | None:
    """Get anomaly notification by token

     Return an Anomaly Notification that the current API token has access to.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyNotification | Errors
    """

    return sync_detailed(
        anomaly_notification_token=anomaly_notification_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[AnomalyNotification | Errors]:
    """Get anomaly notification by token

     Return an Anomaly Notification that the current API token has access to.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyNotification | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_notification_token=anomaly_notification_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> AnomalyNotification | Errors | None:
    """Get anomaly notification by token

     Return an Anomaly Notification that the current API token has access to.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyNotification | Errors
    """

    return (
        await asyncio_detailed(
            anomaly_notification_token=anomaly_notification_token,
            client=client,
        )
    ).parsed
