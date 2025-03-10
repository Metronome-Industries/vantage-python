from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_rule import BillingRule
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    billing_rule_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/billing_rules/{billing_rule_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillingRule, Errors]]:
    if response.status_code == 204:
        response_204 = BillingRule.from_dict(response.json())

        return response_204
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BillingRule, Errors]]:
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
) -> Response[Union[BillingRule, Errors]]:
    """Delete a Billing Rule.

    Args:
        billing_rule_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingRule, Errors]]
    """

    kwargs = _get_kwargs(
        billing_rule_token=billing_rule_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BillingRule, Errors]]:
    """Delete a Billing Rule.

    Args:
        billing_rule_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingRule, Errors]
    """

    return sync_detailed(
        billing_rule_token=billing_rule_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BillingRule, Errors]]:
    """Delete a Billing Rule.

    Args:
        billing_rule_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingRule, Errors]]
    """

    kwargs = _get_kwargs(
        billing_rule_token=billing_rule_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_rule_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BillingRule, Errors]]:
    """Delete a Billing Rule.

    Args:
        billing_rule_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingRule, Errors]
    """

    return (
        await asyncio_detailed(
            billing_rule_token=billing_rule_token,
            client=client,
        )
    ).parsed
