import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forecasted_costs import ForecastedCosts
from ...models.get_forecasted_costs_provider import GetForecastedCostsProvider
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cost_report_token: str,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    provider: GetForecastedCostsProvider | Unset = UNSET,
    service: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_provider: str | Unset = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value

    params["provider"] = json_provider

    params["service"] = service

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/cost_reports/{cost_report_token}/forecasted_costs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForecastedCosts | None:
    if response.status_code == 200:
        response_200 = ForecastedCosts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ForecastedCosts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    provider: GetForecastedCostsProvider | Unset = UNSET,
    service: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ForecastedCosts]:
    """Get forecasted costs for a cost report

     Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        provider (GetForecastedCostsProvider | Unset):
        service (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastedCosts]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    provider: GetForecastedCostsProvider | Unset = UNSET,
    service: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ForecastedCosts | None:
    """Get forecasted costs for a cost report

     Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        provider (GetForecastedCostsProvider | Unset):
        service (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastedCosts
    """

    return sync_detailed(
        cost_report_token=cost_report_token,
        client=client,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    provider: GetForecastedCostsProvider | Unset = UNSET,
    service: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ForecastedCosts]:
    """Get forecasted costs for a cost report

     Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        provider (GetForecastedCostsProvider | Unset):
        service (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastedCosts]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    provider: GetForecastedCostsProvider | Unset = UNSET,
    service: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ForecastedCosts | None:
    """Get forecasted costs for a cost report

     Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        provider (GetForecastedCostsProvider | Unset):
        service (str | Unset):
        page (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastedCosts
    """

    return (
        await asyncio_detailed(
            cost_report_token=cost_report_token,
            client=client,
            start_date=start_date,
            end_date=end_date,
            provider=provider,
            service=service,
            page=page,
            limit=limit,
        )
    ).parsed
