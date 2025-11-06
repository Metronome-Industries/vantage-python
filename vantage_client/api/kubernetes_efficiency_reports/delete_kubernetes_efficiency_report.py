from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.kubernetes_efficiency_report import KubernetesEfficiencyReport
from ...types import Response


def _get_kwargs(
    kubernetes_efficiency_report_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/kubernetes_efficiency_reports/{kubernetes_efficiency_report_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | KubernetesEfficiencyReport | None:
    if response.status_code == 204:
        response_204 = KubernetesEfficiencyReport.from_dict(response.json())

        return response_204

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Errors | KubernetesEfficiencyReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kubernetes_efficiency_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | KubernetesEfficiencyReport]:
    """Delete Kubernetes efficiency report

     Delete a KubernetesEfficiencyReport.

    Args:
        kubernetes_efficiency_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | KubernetesEfficiencyReport]
    """

    kwargs = _get_kwargs(
        kubernetes_efficiency_report_token=kubernetes_efficiency_report_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kubernetes_efficiency_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | KubernetesEfficiencyReport | None:
    """Delete Kubernetes efficiency report

     Delete a KubernetesEfficiencyReport.

    Args:
        kubernetes_efficiency_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | KubernetesEfficiencyReport
    """

    return sync_detailed(
        kubernetes_efficiency_report_token=kubernetes_efficiency_report_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    kubernetes_efficiency_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Errors | KubernetesEfficiencyReport]:
    """Delete Kubernetes efficiency report

     Delete a KubernetesEfficiencyReport.

    Args:
        kubernetes_efficiency_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | KubernetesEfficiencyReport]
    """

    kwargs = _get_kwargs(
        kubernetes_efficiency_report_token=kubernetes_efficiency_report_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kubernetes_efficiency_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Errors | KubernetesEfficiencyReport | None:
    """Delete Kubernetes efficiency report

     Delete a KubernetesEfficiencyReport.

    Args:
        kubernetes_efficiency_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | KubernetesEfficiencyReport
    """

    return (
        await asyncio_detailed(
            kubernetes_efficiency_report_token=kubernetes_efficiency_report_token,
            client=client,
        )
    ).parsed
