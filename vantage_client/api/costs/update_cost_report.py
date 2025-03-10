from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_report import CostReport
from ...models.errors import Errors
from ...models.update_cost_report import UpdateCostReport
from ...types import Response


def _get_kwargs(
    cost_report_token: str,
    *,
    body: UpdateCostReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/cost_reports/{cost_report_token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CostReport, Errors]]:
    if response.status_code == 200:
        response_200 = CostReport.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CostReport, Errors]]:
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
    body: UpdateCostReport,
) -> Response[Union[CostReport, Errors]]:
    """Update a CostReport.

    Args:
        cost_report_token (str):
        body (UpdateCostReport): Update a CostReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CostReport, Errors]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostReport,
) -> Optional[Union[CostReport, Errors]]:
    """Update a CostReport.

    Args:
        cost_report_token (str):
        body (UpdateCostReport): Update a CostReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CostReport, Errors]
    """

    return sync_detailed(
        cost_report_token=cost_report_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostReport,
) -> Response[Union[CostReport, Errors]]:
    """Update a CostReport.

    Args:
        cost_report_token (str):
        body (UpdateCostReport): Update a CostReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CostReport, Errors]]
    """

    kwargs = _get_kwargs(
        cost_report_token=cost_report_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_report_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostReport,
) -> Optional[Union[CostReport, Errors]]:
    """Update a CostReport.

    Args:
        cost_report_token (str):
        body (UpdateCostReport): Update a CostReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CostReport, Errors]
    """

    return (
        await asyncio_detailed(
            cost_report_token=cost_report_token,
            client=client,
            body=body,
        )
    ).parsed
