from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_grant import AccessGrant
from ...models.errors import Errors
from ...models.update_access_grant import UpdateAccessGrant
from ...types import Response


def _get_kwargs(
    access_grant_token: str,
    *,
    body: UpdateAccessGrant,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/access_grants/{access_grant_token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccessGrant, Errors]]:
    if response.status_code == 200:
        response_200 = AccessGrant.from_dict(response.json())

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
) -> Response[Union[AccessGrant, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_grant_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccessGrant,
) -> Response[Union[AccessGrant, Errors]]:
    """Update an AccessGrant.

    Args:
        access_grant_token (str):
        body (UpdateAccessGrant): Update an AccessGrant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessGrant, Errors]]
    """

    kwargs = _get_kwargs(
        access_grant_token=access_grant_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_grant_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccessGrant,
) -> Optional[Union[AccessGrant, Errors]]:
    """Update an AccessGrant.

    Args:
        access_grant_token (str):
        body (UpdateAccessGrant): Update an AccessGrant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessGrant, Errors]
    """

    return sync_detailed(
        access_grant_token=access_grant_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    access_grant_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccessGrant,
) -> Response[Union[AccessGrant, Errors]]:
    """Update an AccessGrant.

    Args:
        access_grant_token (str):
        body (UpdateAccessGrant): Update an AccessGrant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessGrant, Errors]]
    """

    kwargs = _get_kwargs(
        access_grant_token=access_grant_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_grant_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAccessGrant,
) -> Optional[Union[AccessGrant, Errors]]:
    """Update an AccessGrant.

    Args:
        access_grant_token (str):
        body (UpdateAccessGrant): Update an AccessGrant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessGrant, Errors]
    """

    return (
        await asyncio_detailed(
            access_grant_token=access_grant_token,
            client=client,
            body=body,
        )
    ).parsed
