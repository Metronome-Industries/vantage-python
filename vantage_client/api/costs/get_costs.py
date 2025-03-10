from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.costs import Costs
from ...models.errors import Errors
from ...models.get_costs_date_bin import GetCostsDateBin
from ...models.get_costs_order import GetCostsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    groupings: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, GetCostsOrder] = GetCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    date_bin: Union[Unset, GetCostsDateBin] = UNSET,
    settingsinclude_credits: Union[Unset, bool] = False,
    settingsinclude_refunds: Union[Unset, bool] = False,
    settingsinclude_discounts: Union[Unset, bool] = True,
    settingsinclude_tax: Union[Unset, bool] = True,
    settingsamortize: Union[Unset, bool] = True,
    settingsunallocated: Union[Unset, bool] = False,
    settingsaggregate_by: Union[Unset, str] = "cost",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cost_report_token"] = cost_report_token

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_groupings: Union[Unset, list[str]] = UNSET
    if not isinstance(groupings, Unset):
        json_groupings = groupings

    params["groupings"] = json_groupings

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["limit"] = limit

    json_date_bin: Union[Unset, str] = UNSET
    if not isinstance(date_bin, Unset):
        json_date_bin = date_bin.value

    params["date_bin"] = json_date_bin

    params["settings[include_credits]"] = settingsinclude_credits

    params["settings[include_refunds]"] = settingsinclude_refunds

    params["settings[include_discounts]"] = settingsinclude_discounts

    params["settings[include_tax]"] = settingsinclude_tax

    params["settings[amortize]"] = settingsamortize

    params["settings[unallocated]"] = settingsunallocated

    params["settings[aggregate_by]"] = settingsaggregate_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/costs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Costs, Errors]]:
    if response.status_code == 200:
        response_200 = Costs.from_dict(response.json())

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
) -> Response[Union[Costs, Errors]]:
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
    groupings: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, GetCostsOrder] = GetCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    date_bin: Union[Unset, GetCostsDateBin] = UNSET,
    settingsinclude_credits: Union[Unset, bool] = False,
    settingsinclude_refunds: Union[Unset, bool] = False,
    settingsinclude_discounts: Union[Unset, bool] = True,
    settingsinclude_tax: Union[Unset, bool] = True,
    settingsamortize: Union[Unset, bool] = True,
    settingsunallocated: Union[Unset, bool] = False,
    settingsaggregate_by: Union[Unset, str] = "cost",
) -> Response[Union[Costs, Errors]]:
    """Return all Costs for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        groupings (Union[Unset, list[str]]):
        order (Union[Unset, GetCostsOrder]):  Default: GetCostsOrder.DESC.
        limit (Union[Unset, int]):
        date_bin (Union[Unset, GetCostsDateBin]):
        settingsinclude_credits (Union[Unset, bool]):  Default: False.
        settingsinclude_refunds (Union[Unset, bool]):  Default: False.
        settingsinclude_discounts (Union[Unset, bool]):  Default: True.
        settingsinclude_tax (Union[Unset, bool]):  Default: True.
        settingsamortize (Union[Unset, bool]):  Default: True.
        settingsunallocated (Union[Unset, bool]):  Default: False.
        settingsaggregate_by (Union[Unset, str]):  Default: 'cost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Costs, Errors]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
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
    groupings: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, GetCostsOrder] = GetCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    date_bin: Union[Unset, GetCostsDateBin] = UNSET,
    settingsinclude_credits: Union[Unset, bool] = False,
    settingsinclude_refunds: Union[Unset, bool] = False,
    settingsinclude_discounts: Union[Unset, bool] = True,
    settingsinclude_tax: Union[Unset, bool] = True,
    settingsamortize: Union[Unset, bool] = True,
    settingsunallocated: Union[Unset, bool] = False,
    settingsaggregate_by: Union[Unset, str] = "cost",
) -> Optional[Union[Costs, Errors]]:
    """Return all Costs for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        groupings (Union[Unset, list[str]]):
        order (Union[Unset, GetCostsOrder]):  Default: GetCostsOrder.DESC.
        limit (Union[Unset, int]):
        date_bin (Union[Unset, GetCostsDateBin]):
        settingsinclude_credits (Union[Unset, bool]):  Default: False.
        settingsinclude_refunds (Union[Unset, bool]):  Default: False.
        settingsinclude_discounts (Union[Unset, bool]):  Default: True.
        settingsinclude_tax (Union[Unset, bool]):  Default: True.
        settingsamortize (Union[Unset, bool]):  Default: True.
        settingsunallocated (Union[Unset, bool]):  Default: False.
        settingsaggregate_by (Union[Unset, str]):  Default: 'cost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Costs, Errors]
    """

    return sync_detailed(
        client=client,
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    groupings: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, GetCostsOrder] = GetCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    date_bin: Union[Unset, GetCostsDateBin] = UNSET,
    settingsinclude_credits: Union[Unset, bool] = False,
    settingsinclude_refunds: Union[Unset, bool] = False,
    settingsinclude_discounts: Union[Unset, bool] = True,
    settingsinclude_tax: Union[Unset, bool] = True,
    settingsamortize: Union[Unset, bool] = True,
    settingsunallocated: Union[Unset, bool] = False,
    settingsaggregate_by: Union[Unset, str] = "cost",
) -> Response[Union[Costs, Errors]]:
    """Return all Costs for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        groupings (Union[Unset, list[str]]):
        order (Union[Unset, GetCostsOrder]):  Default: GetCostsOrder.DESC.
        limit (Union[Unset, int]):
        date_bin (Union[Unset, GetCostsDateBin]):
        settingsinclude_credits (Union[Unset, bool]):  Default: False.
        settingsinclude_refunds (Union[Unset, bool]):  Default: False.
        settingsinclude_discounts (Union[Unset, bool]):  Default: True.
        settingsinclude_tax (Union[Unset, bool]):  Default: True.
        settingsamortize (Union[Unset, bool]):  Default: True.
        settingsunallocated (Union[Unset, bool]):  Default: False.
        settingsaggregate_by (Union[Unset, str]):  Default: 'cost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Costs, Errors]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cost_report_token: str,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    groupings: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, GetCostsOrder] = GetCostsOrder.DESC,
    limit: Union[Unset, int] = UNSET,
    date_bin: Union[Unset, GetCostsDateBin] = UNSET,
    settingsinclude_credits: Union[Unset, bool] = False,
    settingsinclude_refunds: Union[Unset, bool] = False,
    settingsinclude_discounts: Union[Unset, bool] = True,
    settingsinclude_tax: Union[Unset, bool] = True,
    settingsamortize: Union[Unset, bool] = True,
    settingsunallocated: Union[Unset, bool] = False,
    settingsaggregate_by: Union[Unset, str] = "cost",
) -> Optional[Union[Costs, Errors]]:
    """Return all Costs for a CostReport.

    Args:
        cost_report_token (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        groupings (Union[Unset, list[str]]):
        order (Union[Unset, GetCostsOrder]):  Default: GetCostsOrder.DESC.
        limit (Union[Unset, int]):
        date_bin (Union[Unset, GetCostsDateBin]):
        settingsinclude_credits (Union[Unset, bool]):  Default: False.
        settingsinclude_refunds (Union[Unset, bool]):  Default: False.
        settingsinclude_discounts (Union[Unset, bool]):  Default: True.
        settingsinclude_tax (Union[Unset, bool]):  Default: True.
        settingsamortize (Union[Unset, bool]):  Default: True.
        settingsunallocated (Union[Unset, bool]):  Default: False.
        settingsaggregate_by (Union[Unset, str]):  Default: 'cost'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Costs, Errors]
    """

    return (
        await asyncio_detailed(
            client=client,
            cost_report_token=cost_report_token,
            start_date=start_date,
            end_date=end_date,
            groupings=groupings,
            order=order,
            limit=limit,
            date_bin=date_bin,
            settingsinclude_credits=settingsinclude_credits,
            settingsinclude_refunds=settingsinclude_refunds,
            settingsinclude_discounts=settingsinclude_discounts,
            settingsinclude_tax=settingsinclude_tax,
            settingsamortize=settingsamortize,
            settingsunallocated=settingsunallocated,
            settingsaggregate_by=settingsaggregate_by,
        )
    ).parsed
