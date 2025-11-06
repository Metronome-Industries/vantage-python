from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.network_flow_report import NetworkFlowReport
from ...models.update_network_flow_report import UpdateNetworkFlowReport
from ...types import Response


def _get_kwargs(
    network_flow_report_token: str,
    *,
    body: UpdateNetworkFlowReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/network_flow_reports/{network_flow_report_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | NetworkFlowReport | None:
    if response.status_code == 200:
        response_200 = NetworkFlowReport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | NetworkFlowReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    network_flow_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateNetworkFlowReport,
) -> Response[Errors | NetworkFlowReport]:
    """Update network flow report

     Update a NetworkFlowReport.

    Args:
        network_flow_report_token (str):
        body (UpdateNetworkFlowReport): Update a NetworkFlowReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | NetworkFlowReport]
    """

    kwargs = _get_kwargs(
        network_flow_report_token=network_flow_report_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    network_flow_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateNetworkFlowReport,
) -> Errors | NetworkFlowReport | None:
    """Update network flow report

     Update a NetworkFlowReport.

    Args:
        network_flow_report_token (str):
        body (UpdateNetworkFlowReport): Update a NetworkFlowReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | NetworkFlowReport
    """

    return sync_detailed(
        network_flow_report_token=network_flow_report_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    network_flow_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateNetworkFlowReport,
) -> Response[Errors | NetworkFlowReport]:
    """Update network flow report

     Update a NetworkFlowReport.

    Args:
        network_flow_report_token (str):
        body (UpdateNetworkFlowReport): Update a NetworkFlowReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | NetworkFlowReport]
    """

    kwargs = _get_kwargs(
        network_flow_report_token=network_flow_report_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    network_flow_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateNetworkFlowReport,
) -> Errors | NetworkFlowReport | None:
    """Update network flow report

     Update a NetworkFlowReport.

    Args:
        network_flow_report_token (str):
        body (UpdateNetworkFlowReport): Update a NetworkFlowReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | NetworkFlowReport
    """

    return (
        await asyncio_detailed(
            network_flow_report_token=network_flow_report_token,
            client=client,
            body=body,
        )
    ).parsed
