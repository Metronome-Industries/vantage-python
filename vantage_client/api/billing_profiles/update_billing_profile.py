from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_profile import BillingProfile
from ...models.errors import Errors
from ...models.update_billing_profile_body import UpdateBillingProfileBody
from ...types import Response


def _get_kwargs(
    billing_profile_token: str,
    *,
    body: UpdateBillingProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/billing_profiles/{billing_profile_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillingProfile, Errors]]:
    if response.status_code == 200:
        response_200 = BillingProfile.from_dict(response.json())

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
) -> Response[Union[BillingProfile, Errors]]:
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
    body: UpdateBillingProfileBody,
) -> Response[Union[BillingProfile, Errors]]:
    """Update a Billing Profile.

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):
        body (UpdateBillingProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingProfile, Errors]]
    """

    kwargs = _get_kwargs(
        billing_profile_token=billing_profile_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingProfileBody,
) -> Optional[Union[BillingProfile, Errors]]:
    """Update a Billing Profile.

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):
        body (UpdateBillingProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingProfile, Errors]
    """

    return sync_detailed(
        billing_profile_token=billing_profile_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingProfileBody,
) -> Response[Union[BillingProfile, Errors]]:
    """Update a Billing Profile.

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):
        body (UpdateBillingProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingProfile, Errors]]
    """

    kwargs = _get_kwargs(
        billing_profile_token=billing_profile_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_profile_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillingProfileBody,
) -> Optional[Union[BillingProfile, Errors]]:
    """Update a Billing Profile.

     Requires MSP invoicing to be enabled on the account.

    Args:
        billing_profile_token (str):
        body (UpdateBillingProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingProfile, Errors]
    """

    return (
        await asyncio_detailed(
            billing_profile_token=billing_profile_token,
            client=client,
            body=body,
        )
    ).parsed
