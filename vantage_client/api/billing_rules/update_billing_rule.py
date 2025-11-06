from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_rule import BillingRule
from ...models.errors import Errors
from ...models.update_billing_rule import UpdateBillingRule
from ...types import Response


def _get_kwargs(
    billing_rule_token: str,
    *,
    body: UpdateBillingRule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/billing_rules/{billing_rule_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BillingRule | Errors | None:
    if response.status_code == 200:
        response_200 = BillingRule.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BillingRule | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingRule,
) -> Response[BillingRule | Errors]:
    """Update billing rule

     Update a BillingRule.

    Args:
        billing_rule_token (str):
        body (UpdateBillingRule): Update a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingRule | Errors]
    """

    kwargs = _get_kwargs(
        billing_rule_token=billing_rule_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingRule,
) -> BillingRule | Errors | None:
    """Update billing rule

     Update a BillingRule.

    Args:
        billing_rule_token (str):
        body (UpdateBillingRule): Update a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingRule | Errors
    """

    return sync_detailed(
        billing_rule_token=billing_rule_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingRule,
) -> Response[BillingRule | Errors]:
    """Update billing rule

     Update a BillingRule.

    Args:
        billing_rule_token (str):
        body (UpdateBillingRule): Update a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingRule | Errors]
    """

    kwargs = _get_kwargs(
        billing_rule_token=billing_rule_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingRule,
) -> BillingRule | Errors | None:
    """Update billing rule

     Update a BillingRule.

    Args:
        billing_rule_token (str):
        body (UpdateBillingRule): Update a BillingRule.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingRule | Errors
    """

    return (
        await asyncio_detailed(
            billing_rule_token=billing_rule_token,
            client=client,
            body=body,
        )
    ).parsed
