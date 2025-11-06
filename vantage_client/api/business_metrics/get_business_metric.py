from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_metric import BusinessMetric
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    business_metric_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/business_metrics/{business_metric_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessMetric | Errors | None:
    if response.status_code == 200:
        response_200 = BusinessMetric.from_dict(response.json())

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
) -> Response[BusinessMetric | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BusinessMetric | Errors]:
    """Get business metric by token

     Return a BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetric | Errors]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
) -> BusinessMetric | Errors | None:
    """Get business metric by token

     Return a BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetric | Errors
    """

    return sync_detailed(
        business_metric_token=business_metric_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BusinessMetric | Errors]:
    """Get business metric by token

     Return a BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetric | Errors]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
) -> BusinessMetric | Errors | None:
    """Get business metric by token

     Return a BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetric | Errors
    """

    return (
        await asyncio_detailed(
            business_metric_token=business_metric_token,
            client=client,
        )
    ).parsed
