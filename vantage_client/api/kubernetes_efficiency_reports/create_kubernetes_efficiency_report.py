from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_kubernetes_efficiency_report import CreateKubernetesEfficiencyReport
from ...models.errors import Errors
from ...models.kubernetes_efficiency_report import KubernetesEfficiencyReport
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKubernetesEfficiencyReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kubernetes_efficiency_reports",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, KubernetesEfficiencyReport]]:
    if response.status_code == 201:
        response_201 = KubernetesEfficiencyReport.from_dict(response.json())

        return response_201
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, KubernetesEfficiencyReport]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKubernetesEfficiencyReport,
) -> Response[Union[Errors, KubernetesEfficiencyReport]]:
    """Create a KubernetesEfficiencyReport.

    Args:
        body (CreateKubernetesEfficiencyReport): Create a KubernetesEfficiencyReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, KubernetesEfficiencyReport]]
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
    body: CreateKubernetesEfficiencyReport,
) -> Optional[Union[Errors, KubernetesEfficiencyReport]]:
    """Create a KubernetesEfficiencyReport.

    Args:
        body (CreateKubernetesEfficiencyReport): Create a KubernetesEfficiencyReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, KubernetesEfficiencyReport]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKubernetesEfficiencyReport,
) -> Response[Union[Errors, KubernetesEfficiencyReport]]:
    """Create a KubernetesEfficiencyReport.

    Args:
        body (CreateKubernetesEfficiencyReport): Create a KubernetesEfficiencyReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, KubernetesEfficiencyReport]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateKubernetesEfficiencyReport,
) -> Optional[Union[Errors, KubernetesEfficiencyReport]]:
    """Create a KubernetesEfficiencyReport.

    Args:
        body (CreateKubernetesEfficiencyReport): Create a KubernetesEfficiencyReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, KubernetesEfficiencyReport]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
