from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost import Cost
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    integration_token: str,
    user_costs_upload_token: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/integrations/{integration_token}/costs/{user_costs_upload_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Cost, Errors]]:
    if response.status_code == 204:
        response_204 = Cost.from_dict(response.json())

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
) -> Response[Union[Cost, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_token: str,
    user_costs_upload_token: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Cost, Errors]]:
    """Delete a UserCostsUpload.

    Args:
        integration_token (str):
        user_costs_upload_token (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Cost, Errors]]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
        user_costs_upload_token=user_costs_upload_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_token: str,
    user_costs_upload_token: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Cost, Errors]]:
    """Delete a UserCostsUpload.

    Args:
        integration_token (str):
        user_costs_upload_token (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Cost, Errors]
    """

    return sync_detailed(
        integration_token=integration_token,
        user_costs_upload_token=user_costs_upload_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    integration_token: str,
    user_costs_upload_token: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Cost, Errors]]:
    """Delete a UserCostsUpload.

    Args:
        integration_token (str):
        user_costs_upload_token (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Cost, Errors]]
    """

    kwargs = _get_kwargs(
        integration_token=integration_token,
        user_costs_upload_token=user_costs_upload_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_token: str,
    user_costs_upload_token: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Cost, Errors]]:
    """Delete a UserCostsUpload.

    Args:
        integration_token (str):
        user_costs_upload_token (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Cost, Errors]
    """

    return (
        await asyncio_detailed(
            integration_token=integration_token,
            user_costs_upload_token=user_costs_upload_token,
            client=client,
        )
    ).parsed
