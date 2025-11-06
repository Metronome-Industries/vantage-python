from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.get_costs_date_bin import GetCostsDateBin
from ...models.get_costs_order import GetCostsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cost_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    groupings: list[str] | Unset = UNSET,
    order: GetCostsOrder | Unset = GetCostsOrder.DESC,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    date_bin: GetCostsDateBin | Unset = UNSET,
    settingsinclude_credits: bool | Unset = False,
    settingsinclude_refunds: bool | Unset = False,
    settingsinclude_discounts: bool | Unset = True,
    settingsinclude_tax: bool | Unset = True,
    settingsamortize: bool | Unset = True,
    settingsunallocated: bool | Unset = False,
    settingsaggregate_by: str | Unset = "cost",
    settingsshow_previous_period: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cost_report_token"] = cost_report_token

    params["filter"] = filter_

    params["workspace_token"] = workspace_token

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_groupings: list[str] | Unset = UNSET
    if not isinstance(groupings, Unset):
        json_groupings = groupings

    params["groupings"] = json_groupings

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["limit"] = limit

    params["page"] = page

    json_date_bin: str | Unset = UNSET
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

    params["settings[show_previous_period]"] = settingsshow_previous_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/costs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Errors | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cost_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    groupings: list[str] | Unset = UNSET,
    order: GetCostsOrder | Unset = GetCostsOrder.DESC,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    date_bin: GetCostsDateBin | Unset = UNSET,
    settingsinclude_credits: bool | Unset = False,
    settingsinclude_refunds: bool | Unset = False,
    settingsinclude_discounts: bool | Unset = True,
    settingsinclude_tax: bool | Unset = True,
    settingsamortize: bool | Unset = True,
    settingsunallocated: bool | Unset = False,
    settingsaggregate_by: str | Unset = "cost",
    settingsshow_previous_period: bool | Unset = True,
) -> Response[Errors]:
    """Get costs for cost report or VQL filter

     Return all Costs for a CostReport or VQL filter.

    Args:
        cost_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        groupings (list[str] | Unset):
        order (GetCostsOrder | Unset):  Default: GetCostsOrder.DESC.
        limit (int | Unset):
        page (int | Unset):
        date_bin (GetCostsDateBin | Unset):
        settingsinclude_credits (bool | Unset):  Default: False.
        settingsinclude_refunds (bool | Unset):  Default: False.
        settingsinclude_discounts (bool | Unset):  Default: True.
        settingsinclude_tax (bool | Unset):  Default: True.
        settingsamortize (bool | Unset):  Default: True.
        settingsunallocated (bool | Unset):  Default: False.
        settingsaggregate_by (str | Unset):  Default: 'cost'.
        settingsshow_previous_period (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        page=page,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
        settingsshow_previous_period=settingsshow_previous_period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cost_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    groupings: list[str] | Unset = UNSET,
    order: GetCostsOrder | Unset = GetCostsOrder.DESC,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    date_bin: GetCostsDateBin | Unset = UNSET,
    settingsinclude_credits: bool | Unset = False,
    settingsinclude_refunds: bool | Unset = False,
    settingsinclude_discounts: bool | Unset = True,
    settingsinclude_tax: bool | Unset = True,
    settingsamortize: bool | Unset = True,
    settingsunallocated: bool | Unset = False,
    settingsaggregate_by: str | Unset = "cost",
    settingsshow_previous_period: bool | Unset = True,
) -> Errors | None:
    """Get costs for cost report or VQL filter

     Return all Costs for a CostReport or VQL filter.

    Args:
        cost_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        groupings (list[str] | Unset):
        order (GetCostsOrder | Unset):  Default: GetCostsOrder.DESC.
        limit (int | Unset):
        page (int | Unset):
        date_bin (GetCostsDateBin | Unset):
        settingsinclude_credits (bool | Unset):  Default: False.
        settingsinclude_refunds (bool | Unset):  Default: False.
        settingsinclude_discounts (bool | Unset):  Default: True.
        settingsinclude_tax (bool | Unset):  Default: True.
        settingsamortize (bool | Unset):  Default: True.
        settingsunallocated (bool | Unset):  Default: False.
        settingsaggregate_by (str | Unset):  Default: 'cost'.
        settingsshow_previous_period (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors
    """

    return sync_detailed(
        client=client,
        cost_report_token=cost_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        page=page,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
        settingsshow_previous_period=settingsshow_previous_period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cost_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    groupings: list[str] | Unset = UNSET,
    order: GetCostsOrder | Unset = GetCostsOrder.DESC,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    date_bin: GetCostsDateBin | Unset = UNSET,
    settingsinclude_credits: bool | Unset = False,
    settingsinclude_refunds: bool | Unset = False,
    settingsinclude_discounts: bool | Unset = True,
    settingsinclude_tax: bool | Unset = True,
    settingsamortize: bool | Unset = True,
    settingsunallocated: bool | Unset = False,
    settingsaggregate_by: str | Unset = "cost",
    settingsshow_previous_period: bool | Unset = True,
) -> Response[Errors]:
    """Get costs for cost report or VQL filter

     Return all Costs for a CostReport or VQL filter.

    Args:
        cost_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        groupings (list[str] | Unset):
        order (GetCostsOrder | Unset):  Default: GetCostsOrder.DESC.
        limit (int | Unset):
        page (int | Unset):
        date_bin (GetCostsDateBin | Unset):
        settingsinclude_credits (bool | Unset):  Default: False.
        settingsinclude_refunds (bool | Unset):  Default: False.
        settingsinclude_discounts (bool | Unset):  Default: True.
        settingsinclude_tax (bool | Unset):  Default: True.
        settingsamortize (bool | Unset):  Default: True.
        settingsunallocated (bool | Unset):  Default: False.
        settingsaggregate_by (str | Unset):  Default: 'cost'.
        settingsshow_previous_period (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        filter_=filter_,
        workspace_token=workspace_token,
        start_date=start_date,
        end_date=end_date,
        groupings=groupings,
        order=order,
        limit=limit,
        page=page,
        date_bin=date_bin,
        settingsinclude_credits=settingsinclude_credits,
        settingsinclude_refunds=settingsinclude_refunds,
        settingsinclude_discounts=settingsinclude_discounts,
        settingsinclude_tax=settingsinclude_tax,
        settingsamortize=settingsamortize,
        settingsunallocated=settingsunallocated,
        settingsaggregate_by=settingsaggregate_by,
        settingsshow_previous_period=settingsshow_previous_period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cost_report_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    workspace_token: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    groupings: list[str] | Unset = UNSET,
    order: GetCostsOrder | Unset = GetCostsOrder.DESC,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    date_bin: GetCostsDateBin | Unset = UNSET,
    settingsinclude_credits: bool | Unset = False,
    settingsinclude_refunds: bool | Unset = False,
    settingsinclude_discounts: bool | Unset = True,
    settingsinclude_tax: bool | Unset = True,
    settingsamortize: bool | Unset = True,
    settingsunallocated: bool | Unset = False,
    settingsaggregate_by: str | Unset = "cost",
    settingsshow_previous_period: bool | Unset = True,
) -> Errors | None:
    """Get costs for cost report or VQL filter

     Return all Costs for a CostReport or VQL filter.

    Args:
        cost_report_token (str | Unset):
        filter_ (str | Unset):
        workspace_token (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        groupings (list[str] | Unset):
        order (GetCostsOrder | Unset):  Default: GetCostsOrder.DESC.
        limit (int | Unset):
        page (int | Unset):
        date_bin (GetCostsDateBin | Unset):
        settingsinclude_credits (bool | Unset):  Default: False.
        settingsinclude_refunds (bool | Unset):  Default: False.
        settingsinclude_discounts (bool | Unset):  Default: True.
        settingsinclude_tax (bool | Unset):  Default: True.
        settingsamortize (bool | Unset):  Default: True.
        settingsunallocated (bool | Unset):  Default: False.
        settingsaggregate_by (str | Unset):  Default: 'cost'.
        settingsshow_previous_period (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors
    """

    return (
        await asyncio_detailed(
            client=client,
            cost_report_token=cost_report_token,
            filter_=filter_,
            workspace_token=workspace_token,
            start_date=start_date,
            end_date=end_date,
            groupings=groupings,
            order=order,
            limit=limit,
            page=page,
            date_bin=date_bin,
            settingsinclude_credits=settingsinclude_credits,
            settingsinclude_refunds=settingsinclude_refunds,
            settingsinclude_discounts=settingsinclude_discounts,
            settingsinclude_tax=settingsinclude_tax,
            settingsamortize=settingsamortize,
            settingsunallocated=settingsunallocated,
            settingsaggregate_by=settingsaggregate_by,
            settingsshow_previous_period=settingsshow_previous_period,
        )
    ).parsed
