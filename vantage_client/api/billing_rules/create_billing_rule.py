from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_rule import BillingRule
from ...models.create_billing_rule import CreateBillingRule
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    *,
    body: CreateBillingRule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing_rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BillingRule | Errors | None:
    if response.status_code == 201:
        response_201 = BillingRule.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BillingRule | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBillingRule,
) -> Response[BillingRule | Errors]:
    """Create billing rule

     Create a BillingRule.

    Args:
        body (CreateBillingRule): Create a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingRule | Errors]
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
    body: CreateBillingRule,
) -> BillingRule | Errors | None:
    """Create billing rule

     Create a BillingRule.

    Args:
        body (CreateBillingRule): Create a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingRule | Errors
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateBillingRule,
) -> Response[BillingRule | Errors]:
    """Create billing rule

     Create a BillingRule.

    Args:
        body (CreateBillingRule): Create a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingRule | Errors]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateBillingRule,
) -> BillingRule | Errors | None:
    """Create billing rule

     Create a BillingRule.

    Args:
        body (CreateBillingRule): Create a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingRule | Errors
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
