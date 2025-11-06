from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_alert import AnomalyAlert
from ...models.errors import Errors
from ...models.update_anomaly_alert import UpdateAnomalyAlert
from ...types import Response


def _get_kwargs(
    anomaly_alert_token: str,
    *,
    body: UpdateAnomalyAlert,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/anomaly_alerts/{anomaly_alert_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AnomalyAlert | Errors | None:
    if response.status_code == 200:
        response_200 = AnomalyAlert.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnomalyAlert | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyAlert,
) -> Response[AnomalyAlert | Errors]:
    """Update anomaly alert

     Update an AnomalyAlert.

    Args:
        anomaly_alert_token (str):
        body (UpdateAnomalyAlert): Update an AnomalyAlert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyAlert | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_alert_token=anomaly_alert_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyAlert,
) -> AnomalyAlert | Errors | None:
    """Update anomaly alert

     Update an AnomalyAlert.

    Args:
        anomaly_alert_token (str):
        body (UpdateAnomalyAlert): Update an AnomalyAlert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyAlert | Errors
    """

    return sync_detailed(
        anomaly_alert_token=anomaly_alert_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyAlert,
) -> Response[AnomalyAlert | Errors]:
    """Update anomaly alert

     Update an AnomalyAlert.

    Args:
        anomaly_alert_token (str):
        body (UpdateAnomalyAlert): Update an AnomalyAlert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyAlert | Errors]
    """

    kwargs = _get_kwargs(
        anomaly_alert_token=anomaly_alert_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAnomalyAlert,
) -> AnomalyAlert | Errors | None:
    """Update anomaly alert

     Update an AnomalyAlert.

    Args:
        anomaly_alert_token (str):
        body (UpdateAnomalyAlert): Update an AnomalyAlert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyAlert | Errors
    """

    return (
        await asyncio_detailed(
            anomaly_alert_token=anomaly_alert_token,
            client=client,
            body=body,
        )
    ).parsed
