from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_notification import AnomalyNotification
from ...models.errors import Errors
from ...models.update_anomaly_notification import UpdateAnomalyNotification
from ...types import Response


def _get_kwargs(
    anomaly_notification_token: str,
    *,
    body: UpdateAnomalyNotification,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/anomaly_notifications/{anomaly_notification_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnomalyNotification | Errors | None:
    if response.status_code == 200:
        response_200 = AnomalyNotification.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

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
    body: UpdateAnomalyNotification,
) -> Response[AnomalyNotification | Errors]:
    """Update anomaly notification

     Update an Anomaly Notification.

    Args:
        anomaly_notification_token (str):
        body (UpdateAnomalyNotification): Update an Anomaly Notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyNotification | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_notification_token=anomaly_notification_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyNotification,
) -> AnomalyNotification | Errors | None:
    """Update anomaly notification

     Update an Anomaly Notification.

    Args:
        anomaly_notification_token (str):
        body (UpdateAnomalyNotification): Update an Anomaly Notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyNotification | Errors
    """

    return sync_detailed(
        anomaly_notification_token=anomaly_notification_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyNotification,
) -> Response[AnomalyNotification | Errors]:
    """Update anomaly notification

     Update an Anomaly Notification.

    Args:
        anomaly_notification_token (str):
        body (UpdateAnomalyNotification): Update an Anomaly Notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyNotification | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_notification_token=anomaly_notification_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyNotification,
) -> AnomalyNotification | Errors | None:
    """Update anomaly notification

     Update an Anomaly Notification.

    Args:
        anomaly_notification_token (str):
        body (UpdateAnomalyNotification): Update an Anomaly Notification.

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
            body=body,
        )
    ).parsed
