import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_metric_values import BusinessMetricValues
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    business_metric_token: str,
    *,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/business_metrics/{business_metric_token}/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessMetricValues | Errors | None:
    if response.status_code == 200:
        response_200 = BusinessMetricValues.from_dict(response.json())

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
) -> Response[BusinessMetricValues | Errors]:
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
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
) -> Response[BusinessMetricValues | Errors]:
    """Get business metric values

     Return values of a BusinessMetric

    Args:
        business_metric_token (str):
        page (int | Unset):
        limit (int | Unset):
        start_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetricValues | Errors]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
        page=page,
        limit=limit,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
) -> BusinessMetricValues | Errors | None:
    """Get business metric values

     Return values of a BusinessMetric

    Args:
        business_metric_token (str):
        page (int | Unset):
        limit (int | Unset):
        start_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetricValues | Errors
    """

    return sync_detailed(
        business_metric_token=business_metric_token,
        client=client,
        page=page,
        limit=limit,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
) -> Response[BusinessMetricValues | Errors]:
    """Get business metric values

     Return values of a BusinessMetric

    Args:
        business_metric_token (str):
        page (int | Unset):
        limit (int | Unset):
        start_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetricValues | Errors]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
        page=page,
        limit=limit,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
) -> BusinessMetricValues | Errors | None:
    """Get business metric values

     Return values of a BusinessMetric

    Args:
        business_metric_token (str):
        page (int | Unset):
        limit (int | Unset):
        start_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetricValues | Errors
    """

    return (
        await asyncio_detailed(
            business_metric_token=business_metric_token,
            client=client,
            page=page,
            limit=limit,
            start_date=start_date,
        )
    ).parsed
