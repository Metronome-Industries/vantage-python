from http import HTTPStatus
from typing import Any, Optional, Union

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
        "method": "delete",
        "url": f"/anomaly_notifications/{anomaly_notification_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AnomalyNotification, Errors]]:
    if response.status_code == 204:
        response_204 = AnomalyNotification.from_dict(response.json())

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
) -> Response[Union[AnomalyNotification, Errors]]:
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
) -> Response[Union[AnomalyNotification, Errors]]:
    """Delete an Anomaly Notification.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyNotification, Errors]]
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
) -> Optional[Union[AnomalyNotification, Errors]]:
    """Delete an Anomaly Notification.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyNotification, Errors]
    """

    return sync_detailed(
        anomaly_notification_token=anomaly_notification_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    anomaly_notification_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AnomalyNotification, Errors]]:
    """Delete an Anomaly Notification.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyNotification, Errors]]
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
) -> Optional[Union[AnomalyNotification, Errors]]:
    """Delete an Anomaly Notification.

    Args:
        anomaly_notification_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyNotification, Errors]
    """

    return (
        await asyncio_detailed(
            anomaly_notification_token=anomaly_notification_token,
            client=client,
        )
    ).parsed
