from http import HTTPStatus
from typing import Any, Optional, Union

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
        "method": "delete",
        "url": f"/business_metrics/{business_metric_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BusinessMetric, Errors]]:
    if response.status_code == 204:
        response_204 = BusinessMetric.from_dict(response.json())

        return response_204
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BusinessMetric, Errors]]:
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
) -> Response[Union[BusinessMetric, Errors]]:
    """Deletes an existing BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BusinessMetric, Errors]]
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
) -> Optional[Union[BusinessMetric, Errors]]:
    """Deletes an existing BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BusinessMetric, Errors]
    """

    return sync_detailed(
        business_metric_token=business_metric_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BusinessMetric, Errors]]:
    """Deletes an existing BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BusinessMetric, Errors]]
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
) -> Optional[Union[BusinessMetric, Errors]]:
    """Deletes an existing BusinessMetric.

    Args:
        business_metric_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BusinessMetric, Errors]
    """

    return (
        await asyncio_detailed(
            business_metric_token=business_metric_token,
            client=client,
        )
    ).parsed
