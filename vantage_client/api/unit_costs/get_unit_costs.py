from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.get_unit_costs_date_bin import GetUnitCostsDateBin
from ...models.get_unit_costs_order import GetUnitCostsOrder
from ...models.unit_costs import UnitCosts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    date_bin: Union[Unset, GetUnitCostsDateBin] = UNSET,
    order: Union[Unset, GetUnitCostsOrder] = GetUnitCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cost_report_token"] = cost_report_token

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_date_bin: Union[Unset, str] = UNSET
    if not isinstance(date_bin, Unset):
        json_date_bin = date_bin.value

    params["date_bin"] = json_date_bin

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/unit_costs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, UnitCosts]]:
    if response.status_code == 200:
        response_200 = UnitCosts.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 402:
        response_402 = Errors.from_dict(response.json())

        return response_402
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, UnitCosts]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    date_bin: Union[Unset, GetUnitCostsDateBin] = UNSET,
    order: Union[Unset, GetUnitCostsOrder] = GetUnitCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[Union[Errors, UnitCosts]]:
    """Return all UnitCosts for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        date_bin (Union[Unset, GetUnitCostsDateBin]):
        order (Union[Unset, GetUnitCostsOrder]):  Default: GetUnitCostsOrder.DESC.
        limit (Union[Unset, int]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, UnitCosts]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        date_bin=date_bin,
        order=order,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    date_bin: Union[Unset, GetUnitCostsDateBin] = UNSET,
    order: Union[Unset, GetUnitCostsOrder] = GetUnitCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[Union[Errors, UnitCosts]]:
    """Return all UnitCosts for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        date_bin (Union[Unset, GetUnitCostsDateBin]):
        order (Union[Unset, GetUnitCostsOrder]):  Default: GetUnitCostsOrder.DESC.
        limit (Union[Unset, int]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, UnitCosts]
    """

    return sync_detailed(
        client=client,
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        date_bin=date_bin,
        order=order,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    date_bin: Union[Unset, GetUnitCostsDateBin] = UNSET,
    order: Union[Unset, GetUnitCostsOrder] = GetUnitCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Response[Union[Errors, UnitCosts]]:
    """Return all UnitCosts for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        date_bin (Union[Unset, GetUnitCostsDateBin]):
        order (Union[Unset, GetUnitCostsOrder]):  Default: GetUnitCostsOrder.DESC.
        limit (Union[Unset, int]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, UnitCosts]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        date_bin=date_bin,
        order=order,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    date_bin: Union[Unset, GetUnitCostsDateBin] = UNSET,
    order: Union[Unset, GetUnitCostsOrder] = GetUnitCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Optional[Union[Errors, UnitCosts]]:
    """Return all UnitCosts for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        date_bin (Union[Unset, GetUnitCostsDateBin]):
        order (Union[Unset, GetUnitCostsOrder]):  Default: GetUnitCostsOrder.DESC.
        limit (Union[Unset, int]):
        page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, UnitCosts]
    """

    return (
        await asyncio_detailed(
            client=client,
            cost_report_token=cost_report_token,
            start_date=start_date,
            end_date=end_date,
            date_bin=date_bin,
            order=order,
            limit=limit,
            page=page,
        )
    ).parsed
