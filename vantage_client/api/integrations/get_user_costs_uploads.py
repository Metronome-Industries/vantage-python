from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_costs_uploads import UserCostsUploads
from ...types import Response


def _get_kwargs(
    integration_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/integrations/{integration_token}/costs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserCostsUploads]:
    if response.status_code == 200:
        response_200 = UserCostsUploads.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserCostsUploads]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserCostsUploads]:
    """List UserCostUploads.

    Args:
        integration_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserCostsUploads]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UserCostsUploads]:
    """List UserCostUploads.

    Args:
        integration_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserCostsUploads
    """

    return sync_detailed(
        integration_token=integration_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    integration_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserCostsUploads]:
    """List UserCostUploads.

    Args:
        integration_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserCostsUploads]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UserCostsUploads]:
    """List UserCostUploads.

    Args:
        integration_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserCostsUploads
    """

    return (
        await asyncio_detailed(
            integration_token=integration_token,
            client=client,
        )
    ).parsed
