from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_financial_commitment_report import CreateFinancialCommitmentReport
from ...models.errors import Errors
from ...models.financial_commitment_report import FinancialCommitmentReport
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFinancialCommitmentReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/financial_commitment_reports",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    if response.status_code == 201:
        response_201 = FinancialCommitmentReport.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, FinancialCommitmentReport]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFinancialCommitmentReport,
) -> Response[Union[Errors, FinancialCommitmentReport]]:
    """Create a FinancialCommitmentReport.

    Args:
        body (CreateFinancialCommitmentReport): Create a FinancialCommitmentReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, FinancialCommitmentReport]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateFinancialCommitmentReport,
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    """Create a FinancialCommitmentReport.

    Args:
        body (CreateFinancialCommitmentReport): Create a FinancialCommitmentReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, FinancialCommitmentReport]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFinancialCommitmentReport,
) -> Response[Union[Errors, FinancialCommitmentReport]]:
    """Create a FinancialCommitmentReport.

    Args:
        body (CreateFinancialCommitmentReport): Create a FinancialCommitmentReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, FinancialCommitmentReport]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateFinancialCommitmentReport,
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    """Create a FinancialCommitmentReport.

    Args:
        body (CreateFinancialCommitmentReport): Create a FinancialCommitmentReport.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, FinancialCommitmentReport]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
