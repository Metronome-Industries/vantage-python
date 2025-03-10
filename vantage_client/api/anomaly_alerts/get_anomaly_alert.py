from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_alert import AnomalyAlert
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    anomaly_alert_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/anomaly_alerts/{anomaly_alert_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AnomalyAlert, Errors]]:
    if response.status_code == 200:
        response_200 = AnomalyAlert.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AnomalyAlert, Errors]]:
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
) -> Response[Union[AnomalyAlert, Errors]]:
    """Return an AnomalyAlert that the current API token has access to.

    Args:
        anomaly_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyAlert, Errors]]
    """

    kwargs = _get_kwargs(
        anomaly_alert_token=anomaly_alert_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AnomalyAlert, Errors]]:
    """Return an AnomalyAlert that the current API token has access to.

    Args:
        anomaly_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyAlert, Errors]
    """

    return sync_detailed(
        anomaly_alert_token=anomaly_alert_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AnomalyAlert, Errors]]:
    """Return an AnomalyAlert that the current API token has access to.

    Args:
        anomaly_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnomalyAlert, Errors]]
    """

    kwargs = _get_kwargs(
        anomaly_alert_token=anomaly_alert_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anomaly_alert_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AnomalyAlert, Errors]]:
    """Return an AnomalyAlert that the current API token has access to.

    Args:
        anomaly_alert_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnomalyAlert, Errors]
    """

    return (
        await asyncio_detailed(
            anomaly_alert_token=anomaly_alert_token,
            client=client,
        )
    ).parsed
