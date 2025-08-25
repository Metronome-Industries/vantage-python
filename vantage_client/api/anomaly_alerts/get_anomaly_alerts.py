import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.anomaly_alerts import AnomalyAlerts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    cost_category: Union[Unset, str] = UNSET,
    cost_report_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["provider"] = provider

    params["service"] = service

    params["cost_category"] = cost_category

    params["cost_report_token"] = cost_report_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/anomaly_alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AnomalyAlerts]:
    if response.status_code == 200:
        response_200 = AnomalyAlerts.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AnomalyAlerts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    cost_category: Union[Unset, str] = UNSET,
    cost_report_token: Union[Unset, str] = UNSET,
) -> Response[AnomalyAlerts]:
    """Return all Anomaly Alerts that the current API token has access to.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, str]):
        service (Union[Unset, str]):
        cost_category (Union[Unset, str]):
        cost_report_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyAlerts]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        cost_category=cost_category,
        cost_report_token=cost_report_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    cost_category: Union[Unset, str] = UNSET,
    cost_report_token: Union[Unset, str] = UNSET,
) -> Optional[AnomalyAlerts]:
    """Return all Anomaly Alerts that the current API token has access to.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, str]):
        service (Union[Unset, str]):
        cost_category (Union[Unset, str]):
        cost_report_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyAlerts
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        cost_category=cost_category,
        cost_report_token=cost_report_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    cost_category: Union[Unset, str] = UNSET,
    cost_report_token: Union[Unset, str] = UNSET,
) -> Response[AnomalyAlerts]:
    """Return all Anomaly Alerts that the current API token has access to.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, str]):
        service (Union[Unset, str]):
        cost_category (Union[Unset, str]):
        cost_report_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnomalyAlerts]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        provider=provider,
        service=service,
        cost_category=cost_category,
        cost_report_token=cost_report_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    provider: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    cost_category: Union[Unset, str] = UNSET,
    cost_report_token: Union[Unset, str] = UNSET,
) -> Optional[AnomalyAlerts]:
    """Return all Anomaly Alerts that the current API token has access to.

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        provider (Union[Unset, str]):
        service (Union[Unset, str]):
        cost_category (Union[Unset, str]):
        cost_report_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnomalyAlerts
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            provider=provider,
            service=service,
            cost_category=cost_category,
            cost_report_token=cost_report_token,
        )
    ).parsed
