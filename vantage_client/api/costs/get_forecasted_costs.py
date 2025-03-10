import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_reports import CostReports
from ...models.get_forecasted_costs_provider import GetForecastedCostsProvider
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cost_report_token: str,
    *,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, GetForecastedCostsProvider] = UNSET,
    service: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_provider: Union[Unset, str] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value

    params["provider"] = json_provider

    params["service"] = service

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/cost_reports/{cost_report_token}/forecasted_costs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[CostReports]:
    if response.status_code == 200:
        response_200 = CostReports.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CostReports]:
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
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, GetForecastedCostsProvider] = UNSET,
    service: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[CostReports]:
    """Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, GetForecastedCostsProvider]):
        service (Union[Unset, str]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostReports]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
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
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, GetForecastedCostsProvider] = UNSET,
    service: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[CostReports]:
    """Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, GetForecastedCostsProvider]):
        service (Union[Unset, str]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostReports
    """

    return sync_detailed(
        cost_report_token=cost_report_token,
        client=client,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, GetForecastedCostsProvider] = UNSET,
    service: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[CostReports]:
    """Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, GetForecastedCostsProvider]):
        service (Union[Unset, str]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostReports]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, GetForecastedCostsProvider] = UNSET,
    service: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[CostReports]:
    """Return all ForecastedCosts.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, GetForecastedCostsProvider]):
        service (Union[Unset, str]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostReports
    """

    return (
        await asyncio_detailed(
            cost_report_token=cost_report_token,
            client=client,
            start_date=start_date,
            end_date=end_date,
            provider=provider,
            service=service,
            limit=limit,
        )
    ).parsed
