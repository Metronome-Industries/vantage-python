from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_notification import AnomalyNotification
from ...models.create_anomaly_notification import CreateAnomalyNotification
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAnomalyNotification,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/anomaly_notifications",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AnomalyNotification, Errors]]:
    if response.status_code == 201:
        response_201 = AnomalyNotification.from_dict(response.json())

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
) -> Response[Union[AnomalyNotification, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAnomalyNotification,
) -> Response[Union[AnomalyNotification, Errors]]:
    """Create an Anomaly Notification for a Cost Report.

    Args:
        body (CreateAnomalyNotification): Create an Anomaly Notification for a Cost Report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyNotification, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateAnomalyNotification,
) -> Optional[Union[AnomalyNotification, Errors]]:
    """Create an Anomaly Notification for a Cost Report.

    Args:
        body (CreateAnomalyNotification): Create an Anomaly Notification for a Cost Report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyNotification, Errors]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAnomalyNotification,
) -> Response[Union[AnomalyNotification, Errors]]:
    """Create an Anomaly Notification for a Cost Report.

    Args:
        body (CreateAnomalyNotification): Create an Anomaly Notification for a Cost Report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyNotification, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateAnomalyNotification,
) -> Optional[Union[AnomalyNotification, Errors]]:
    """Create an Anomaly Notification for a Cost Report.

    Args:
        body (CreateAnomalyNotification): Create an Anomaly Notification for a Cost Report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyNotification, Errors]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
