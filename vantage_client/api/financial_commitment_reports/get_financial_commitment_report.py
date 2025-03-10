from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.financial_commitment_report import FinancialCommitmentReport
from ...types import Response


def _get_kwargs(
    financial_commitment_report_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/financial_commitment_reports/{financial_commitment_report_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    if response.status_code == 200:
        response_200 = FinancialCommitmentReport.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
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
    financial_commitment_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, FinancialCommitmentReport]]:
    """Return a FinancialCommitmentReport.

    Args:
        financial_commitment_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, FinancialCommitmentReport]]
    """

    kwargs = _get_kwargs(
        financial_commitment_report_token=financial_commitment_report_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    financial_commitment_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    """Return a FinancialCommitmentReport.

    Args:
        financial_commitment_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, FinancialCommitmentReport]
    """

    return sync_detailed(
        financial_commitment_report_token=financial_commitment_report_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    financial_commitment_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, FinancialCommitmentReport]]:
    """Return a FinancialCommitmentReport.

    Args:
        financial_commitment_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, FinancialCommitmentReport]]
    """

    kwargs = _get_kwargs(
        financial_commitment_report_token=financial_commitment_report_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    financial_commitment_report_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, FinancialCommitmentReport]]:
    """Return a FinancialCommitmentReport.

    Args:
        financial_commitment_report_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, FinancialCommitmentReport]
    """

    return (
        await asyncio_detailed(
            financial_commitment_report_token=financial_commitment_report_token,
            client=client,
        )
    ).parsed
