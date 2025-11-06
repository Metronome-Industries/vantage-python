from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_profile import BillingProfile
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    billing_profile_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/billing_profiles/{billing_profile_token}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingProfile | Errors | None:
    if response.status_code == 200:
        response_200 = BillingProfile.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BillingProfile | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BillingProfile | Errors]:
    """Get billing profile by token

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingProfile | Errors]
    """

    kwargs = _get_kwargs(
        billing_profile_token=billing_profile_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
) -> BillingProfile | Errors | None:
    """Get billing profile by token

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingProfile | Errors
    """

    return sync_detailed(
        billing_profile_token=billing_profile_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[BillingProfile | Errors]:
    """Get billing profile by token

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingProfile | Errors]
    """

    kwargs = _get_kwargs(
        billing_profile_token=billing_profile_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
) -> BillingProfile | Errors | None:
    """Get billing profile by token

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingProfile | Errors
    """

    return (
        await asyncio_detailed(
            billing_profile_token=billing_profile_token,
            client=client,
        )
    ).parsed
